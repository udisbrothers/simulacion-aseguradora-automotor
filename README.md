# Modelo y Automatización Actuarial: De Excel a Python

Hola, Soy estudiante del primer semestre de la carrera de Actuario. Este repositorio refleja un proyecto personal que nació de la curiosidad por entender el ciclo completo de los datos en el mercado asegurador: **desde el diseño manual y lógico de una base de datos en Excel hasta su automatización y análisis en Python.**

Dado que estoy dando mis primeros pasos y explorando este campo de forma autodidacta (con apoyo de la Inteligencia Artificial como guía), este desarrollo no busca ser un sistema corporativo, sino el resultado de un proceso de aprendizaje donde quise experimentar cómo se cruzan la teoría de seguros, el diseño de planillas y la programación.

-- Las 2 Etapas del Proyecto --
1. El Modelo Base en Excel (Diseño y Coherencia Actuarial)
Antes de programar, la primera etapa consistió en construir una base de datos simulada de una aseguradora automotor de forma artesanal:

**Generación de datos sintéticos:** Diseñé las solapas de Clientes, Pólizas y Siniestros (300 clientes, 1,000 pólizas y 300 siniestros ). Utilicé una hoja de Listas con rangos de probabilidad y números aleatorios para evitar distribuciones uniformes irreales (por ejemplo, asegurando que ciertos tipos de vehículos o frecuencias de siniestros tuvieran riesgos diferenciados).

**Iteración y depuración:** Como contraparte de usar datos aleatorios, tuve que lidiar con discrepancias constantes y corregirlas ajustando las fórmulas. Un ejemplo fue simplificar las fechas de vencimiento de las pólizas a un año exacto desde su inicio.

**Lógica de negocio y creatividad:** Al tropezar con combinaciones de datos interesantes, agregué capas de complejidad:

  **Fraude sospechado: Una columna lógica dependiente de cruces específicos entre el tipo de siniestro y su gravedad (por ejemplo, combinaciones extrañas como                            "Daños por granizo" y "Muy grave").

  **Días hasta la resolución: Variable relacionada al fraude (si hay sospecha de fraude, los días de resolución aumentan).

  **Validación de coberturas: Cruce para evaluar si la póliza estaba vigente y si el tipo de seguro efectivamente cubría el siniestro reclamado.

  **Depreciación: Impacto de la pérdida de valor del vehículo con el paso de los años sobre el costo del siniestro.

**Hoja "Cálculos":** El panel de control principal en Excel, donde utilicé fórmulas y herramientas nativas para generar métricas visuales como la cantidad de siniestros vs. severidad media y el monto pagado total por tipo de vehículo.

2. La Automatización y Análisis en Python (Pandas & Matplotlib)
Una vez estructurado el Excel, quise llevarlo al siguiente nivel utilizando código para automatizar el procesamiento y la visualización:

**Ingesta multihoja:** Carga de las solapas de Excel utilizando pandas.

**Cruce relacional:** Relación de tablas mediante pd.merge() emulando bases de datos relacionales.

**Métricas actuariales:** Cálculo automatizado de primas totales anuales, severidad promedio, frecuencia y el Loss Ratio (Siniestralidad) agrupado por tipo de vehículo.

Visualización de datos: Gráficos estadísticos con matplotlib, incorporando diseño personalizado (alertas de color según el umbral del Loss Ratio y gráficos de dispersión con coeficiente de correlación de Pearson).

Exportación de reportes: Generación automática de un nuevo archivo de salida (Resultados_Proyecto_Aseguradora.xlsx) con los indicadores procesados.

-- Archivos del Repositorio --
Excel_Proyecto_Aseguradora.xlsx: La base de datos original diseñada e ideada desde cero con datos sintéticos consistentes.

Pyhton_Proyecto_Aseguradora.py: El script de automatización y análisis estadístico.

Resultados_Proyecto_Aseguradora.xlsx: El reporte consolidado exportado automáticamente por el código.

-- Reflexión personal --
Este proyecto me permitió conectar dos mundos: la lógica estructurada de las planillas de cálculo y el poder de escalabilidad de Python. Sé que estoy recién empezando en la carrera y que me queda un camino enorme por recorrer, pero quería dejar plasmado este primer paso de exploración. Cualquier comentario, corrección o consejo es más que bienvenido. ¡Gracias por leer!
