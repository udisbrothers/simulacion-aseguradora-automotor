import pandas as pd
import matplotlib.pyplot as plt

archivo_excel = "Excel_Proyecto_Aseguradora.xlsx"
df_polizas = pd.read_excel(archivo_excel, sheet_name="POLIZAS")
df_clientes = pd.read_excel(archivo_excel, sheet_name="CLIENTES")
df_siniestros = pd.read_excel(archivo_excel, sheet_name="SINIESTROS")

# 1. Promedio de edad por provincia
promedio_edad_asegurados_por_provincia = df_polizas.groupby("PROVINCIA")["EDAD ASEGURADO"].mean()
print("--- Promedio de edad de asegurados por provincia ---")
print(promedio_edad_asegurados_por_provincia)

# 2. Cruce de tablas (Tabla Maestra)
df_merge = pd.merge(df_siniestros, df_polizas, on="ID PÓLIZA", how="left")

# 3. Cálculo de Primas Totales por Tipo de Vehículo (Multiplicando la prima mensual por 12)
prima_por_vehiculo = df_polizas.groupby("TIPO DE VEHICULO")["PRIMA MENSUAL"].sum() * 12

# 4. Agrupamiento de siniestros por Tipo de Vehículo
resumen_vehiculo = df_merge.groupby("TIPO DE VEHICULO_x").agg(
    monto_pagado_total=("IMPORTE PAGADO", "sum"),
    cantidad_siniestros=("ID SINIESTRO", "count"),
    severidad_promedio=("IMPORTE PAGADO", "mean")
)

# 5. Unión de prima total y calculo de el Loss Ratio (Siniestralidad)
resumen_vehiculo["prima_total"] = prima_por_vehiculo
resumen_vehiculo["loss_ratio"] = (resumen_vehiculo["monto_pagado_total"] / resumen_vehiculo["prima_total"]) * 100
monto_en_millones = resumen_vehiculo["monto_pagado_total"] / 1_000_000

# 6. Visualización de los resultados
# Gráfico de barras para el monto pagado total por tipo de vehículo
plt.figure(figsize=(10, 6))
plt.bar(resumen_vehiculo.index, monto_en_millones, color='skyblue', edgecolor='black')
plt.title("Monto Pagado Total por Tipo de Vehículo")
plt.xlabel("Tipo de Vehículo")
plt.ylabel("Monto Pagado Total (En millones de $)")

# 7. Visualizacion 2
plt.figure(figsize=(10, 6))
colores = ["red" if lr > 80 else "green" for lr in resumen_vehiculo["loss_ratio"]]
plt.bar(resumen_vehiculo.index, resumen_vehiculo["loss_ratio"], color=colores, edgecolor='black')
plt.axhline(y=100, color="orange", linestyle="--", label="Punto de equilibrio (100%)")
plt.title("Loss Ratio por Tipo de Vehículo")
plt.xlabel("Tipo de Vehículo")
plt.ylabel("Loss Ratio (%)")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Mostrar el gráfico
plt.tight_layout()
plt.show()

#Siniestros pagados
df_siniestros_pagados = df_merge[df_merge["IMPORTE PAGADO"] > 0]

correlacion = df_siniestros_pagados["EDAD ASEGURADO"].corr(df_siniestros_pagados["IMPORTE PAGADO"])

print(f"\n--- Analisis de correlación ---")
print(f"Coeficiente de Pearson (Edad Asegurado vs Importe Pagado): {correlacion:.4f}")
# Nota: Un valor cerca de 1 es correlación positiva (más edad, más costo). 
# Cerca de -1 es correlación negativa (menos edad, más costo). 
# Cerca de 0 significa que no hay relación lineal.

#Visualización 3 
plt.figure(figsize=(10, 6))
plt.scatter(
    df_siniestros_pagados["EDAD ASEGURADO"],
    df_siniestros_pagados["IMPORTE PAGADO"]/1_000_000,
    alpha=0.6,
    edgecolors='black',)
plt.title(f"Relación entre Edad del Asegurado y Costo del Siniestro\n(Correlación: {correlacion:.2f})")
plt.xlabel("Edad del Asegurado")
plt.ylabel("Importe Pagado (En millones de $)")

plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()


#Creacion de un archivo de salida con los resultados
resumen_vehiculo.to_excel("Resultados_Proyecto_Aseguradora.xlsx", sheet_name="Resumen_vehiculo")
