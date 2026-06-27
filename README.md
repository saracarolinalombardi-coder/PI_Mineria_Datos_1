# Proyecto Integrador — Minería de Datos I

## Información general
Proyecto integrador de la materia Minería de Datos I.
Análisis de datos de usuarios de una plataforma de streaming de América Latina.

## Objetivo del proyecto
Aplicar los contenidos de Minería de Datos I para construir un análisis
de datos reproducible y comunicable. Se busca comprender el comportamiento
de los usuarios de una plataforma de streaming a partir de variables como
edad, plan de suscripción, tiempo de visualización, país de origen,
género favorito y tickets de soporte generados.
El análisis incluye inspección inicial, limpieza, análisis exploratorio,
escalamiento y reducción de dimensionalidad mediante PCA.

## Dataset
El dataset contiene información de 8.160 usuarios de una plataforma de
streaming de América Latina. Incluye 8 variables: user_id, age,
subscription_plan, monthly_watch_time_mins, country, favorite_genre,
last_login_date y customer_support_tickets.
El dataset original presentó problemas de calidad como duplicados,
valores nulos, inconsistencias en variables categóricas y valores
imposibles. Tras el proceso de limpieza se retuvieron 5.886 registros,
representando el 72.1% del total original.
Dataset original disponible en: data/raw/streaming_users_dirty.json
Dataset procesado disponible en: data/processed/streaming_users_clean.csv

## Estructura del repositorio
- data/raw/: dataset original sin modificaciones
- data/processed/: dataset limpio utilizado en el análisis
- notebooks/: desarrollo ordenado de las etapas del proyecto
- app/: aplicación pública desarrollada en Streamlit
- reports/: informe final en PDF
- logs/: registro de transformaciones del proceso ETL

## Preparación y calidad de datos
El proceso de limpieza se documenta en notebooks/02_calidad_y_limpieza.ipynb
y se registra en logs/pipeline_log.csv.
Se identificaron y trataron los siguientes problemas:
- 126 filas duplicadas eliminadas
- Normalización de subscription_plan, country y favorite_genre
- Eliminación de valores imposibles en age y customer_support_tickets
- Imputación de nulos en monthly_watch_time_mins con la mediana (760.8 min)
- Eliminación de fechas inválidas en last_login_date
La retención final del dataset fue del 72.1% (5.886 de 8.160 registros).

## Resumen del análisis exploratorio
El análisis exploratorio se desarrolla en notebooks/03_eda.ipynb.
Se realizaron análisis univariado, bivariado y multivariado.
La distribución de edades se concentra entre 20 y 50 años.
El tiempo de visualización presenta una distribución aproximadamente simétrica
con la mayoría de usuarios entre 400 y 1200 minutos mensuales.
No se observaron diferencias marcadas en el tiempo de visualización
según el plan de suscripción.
El promedio de tickets de soporte varía entre países.
Las variables numéricas no presentan correlaciones fuertes entre sí.

## Reducción de dimensionalidad
El análisis de PCA se desarrolla en notebooks/04_pca.ipynb.
Se aplicó estandarización Z-score sobre las tres variables numéricas
antes de aplicar PCA, siguiendo el criterio de que el escalamiento
es obligatorio antes de PCA.
La varianza explicada se distribuyó de forma uniforme entre los tres
componentes: PC1 33.7%, PC2 33.2% y PC3 33.0%.
Esto indica que las tres variables aportan información independiente
y no redundante al dataset.

## Visualización interactiva
La aplicación pública está disponible en Streamlit Cloud:
Incluye páginas de Dataset, EDA, PCA y Conclusiones con interpretaciones
de cada resultado.

## Cómo ejecutar localmente
1. Clonar el repositorio
2. Crear entorno virtual: python -m venv venv
3. Activar entorno virtual: venv\Scripts\activate
4. Instalar dependencias: pip install -r requirements.txt
5. Ejecutar la app: python -m streamlit run app/Home.py

## Conclusiones
El plan de suscripción no determina el tiempo de visualización mensual.
La edad no presenta relación lineal con el tiempo de consumo.
Los tickets de soporte no reducen significativamente el tiempo de uso.
El PCA confirmó que las tres variables numéricas aportan información
independiente entre sí.
Las conclusiones están condicionadas por la calidad inicial del dataset
y por las decisiones de limpieza documentadas.
