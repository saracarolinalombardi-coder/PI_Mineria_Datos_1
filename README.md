# Proyecto Integrador — Minería de Datos I

## Información general
Este proyecto analiza el comportamiento de usuarios de una plataforma de streaming mediante técnicas de minería de datos. El trabajo incluye desde la inspección inicial de los datos hasta la implementación de una aplicación interactiva con Streamlit, pasando por procesos de limpieza, análisis exploratorio y reducción de dimensionalidad.


## Objetivo del proyecto
El objetivo principal es comprender los patrones de consumo de contenido en una plataforma de streaming, identificando relaciones entre variables demográficas, hábitos de visualización y experiencia del usuario. Específicamente, se busca determinar si el plan de suscripción influye en el tiempo de visualización, si existe relación entre la edad y el consumo, y si los usuarios que generan más tickets de soporte consumen menos contenido. El proyecto culmina en una aplicación interactiva que permite visualizar estos hallazgos.


## Dataset
El dataset original `streaming_users_dirty.json` contiene 8.160 registros y 8 columnas con información de usuarios de una plataforma de streaming. Las variables incluyen: identificador de usuario, edad, plan de suscripción, tiempo mensual de visualización en minutos, país, género favorito, fecha de último login y cantidad de tickets de soporte generados. El dataset presenta problemas de calidad como valores nulos, duplicados, valores imposibles (edades negativas, fechas inválidas) y múltiples variantes inconsistentes en variables categóricas. El dataset se encuentra en la carpeta `data/raw/` y su versión procesada en `data/processed/`.

## Estructura del repositorio
- app/Home.py`: Aplicación principal de Streamlit
- data/raw/`: Datos originales sin modificar
- data/processed/`: Datos limpios y procesados
- logs/pipeline_log.csv`: Registro del proceso ETL aplicado
- notebooks/01_inspeccion_inicial.ipynb`: Análisis inicial del dataset
- notebooks/02_calidad_y_limpieza.ipynb`: Proceso de limpieza y transformación
- notebooks/03_eda.ipynb`: Análisis exploratorio de datos
- notebooks/04_pca.ipynb`: Escalamiento y reducción dimensional
- notebooks/05_conclusiones.ipynb`: Síntesis de hallazgos del análisis
- reports/`: Informes y documentación adicional
- .gitignore`
- README.md`
- requirements.txt`: Dependencias del proyecto


## Preparación y calidad de datos

El proceso de limpieza se documenta en el notebook `02_calidad_y_limpieza.ipynb` y el registro detallado en `logs/pipeline_log.csv`. Se eliminaron 126 filas duplicadas exactas y se normalizaron 15 variantes del plan de suscripción a sus valores canónicos (Básico, Estándar, Premium), 26 variantes de país a 7 países estandarizados y 28 variantes de género favorito a 7 géneros. Los valores nulos se imputaron: 193 valores en tiempo de visualización con la mediana, 240 en género favorito con la moda y 320 en fecha de último login con la mediana de fechas válidas. Se eliminaron 74 registros con edades imposibles (negativas o mayores a 100), 49 con tiempo de visualización negativo y 27 con tickets de soporte negativos. Los outliers extremos en tiempo de visualización y tickets de soporte se trataron mediante winsorización con k=3. El dataset final contiene 7.884 registros con una retención del 96,6% de los datos originales.

## Resumen del análisis exploratorio

El análisis exploratorio se encuentra en el notebook `03_eda.ipynb`. La distribución de edades se concentra entre los 20 y 50 años, con mayor frecuencia en el rango de 25 a 40 años. El tiempo mensual de visualización se distribuye de forma aproximadamente simétrica, con la mayoría de los usuarios entre 400 y 1200 minutos. El mapa de calor de correlaciones mostró que las variables numéricas (edad, tiempo de visualización y tickets de soporte) no presentan correlaciones significativas entre sí. Respecto a las preguntas de análisis, no se encontró evidencia de que el plan de suscripción influya en el tiempo de visualización, ni relación entre la edad y el consumo, ni asociación entre tickets de soporte y menor tiempo de uso. La aplicación Streamlit permite explorar estas visualizaciones de forma interactiva.

## Reducción de dimensionalidad

El análisis de componentes principales se documenta en `04_pca.ipynb`. Se aplicó StandardScaler a las tres variables numéricas (age, monthly_watch_time_mins, customer_support_tickets) debido a sus diferencias de escala. El PCA mostró que cada componente explica aproximadamente un tercio de la varianza (33,75%, 33,22% y 33,03%), lo que indica que las variables no son redundantes entre sí. Para superar el umbral del 80% de varianza acumulada se necesitan las tres componentes originales, por lo que no es posible reducir dimensionalidad sin pérdida significativa de información. La PC1 resume un perfil general del usuario, mientras que la PC2 captura la diferencia entre usuarios mayores con menor consumo frente a jóvenes con mayor consumo.

## Visualización interactiva

La aplicación se encuentra en `app/Home.py` y permite explorar los resultados del análisis mediante visualizaciones interactivas. Incluye gráficos de distribución de variables, análisis por plan de suscripción, comparativas por país y proyecciones del PCA. La aplicación está desplegada en Streamlit Cloud y es accesible a través del siguiente enlace: https://github.com/saracarolinalombardi-coder/PI_Mineria_Datos_1.

## Cómo ejecutar localmente

Clonar el repositorio
Crear entorno virtual: python -m venv venv
Activar entorno virtual: venv\Scripts\activate
Instalar dependencias: pip install -r requirements.txt
Ejecutar la app: python -m streamlit run app/Home.py

## Conclusiones

El análisis nos permitió responder las preguntas planteadas. No se encontró evidencia de que el plan de suscripción influya en el tiempo de visualización mensual, ya que los tres planes presentan distribuciones similares. Tampoco se observó relación entre la edad y el consumo de contenido, ni entre los tickets de soporte y el tiempo de uso de la plataforma. El PCA confirmó que las variables numéricas aportan información independiente, sin lograr una reducción de dimensionalidad significativa. El proceso de limpieza transformó un dataset con múltiples problemas de calidad en un conjunto confiable, con una retención del 96,6% de los registros originales. La aplicación interactiva permite a los usuarios explorar estos hallazgos de manera visual y accesible.