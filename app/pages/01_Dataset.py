import streamlit as st
import pandas as pd

# Cargamos el dataset limpio
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
df = pd.read_csv(os.path.join(BASE_DIR, 'data', 'processed', 'streaming_users_clean.csv'))

st.title("Dataset")

st.markdown("### Descripción general")
st.write("""
El dataset contiene información de usuarios de una plataforma de streaming
de América Latina. Originalmente contaba con 8.160 registros y 8 columnas.
Tras el proceso de limpieza se retuvieron 5.886 registros (72.1% del total).
""")

st.markdown("### Variables del dataset")
st.markdown("""
- **user_id**: identificador único del usuario
- **age**: edad del usuario
- **subscription_plan**: plan contratado (Básico, Estándar, Premium)
- **monthly_watch_time_mins**: tiempo mensual de visualización en minutos
- **country**: país de origen
- **favorite_genre**: género favorito
- **last_login_date**: fecha del último acceso
- **customer_support_tickets**: cantidad de tickets de soporte generados
""")

st.markdown("### Resumen de calidad inicial")
st.markdown("""
El dataset original presentó los siguientes problemas de calidad:
- 126 filas duplicadas
- 753 valores nulos distribuidos en tres columnas
- Inconsistencias en variables categóricas (hasta 26 variantes por variable)
- Valores imposibles en edad, tickets de soporte y tiempo de visualización
- Fechas mal formateadas en last_login_date
""")

st.markdown("### Vista previa del dataset")
st.dataframe(df.head(10))

st.markdown("### Transformaciones principales")
st.markdown("""
1. Eliminación de filas duplicadas
2. Normalización de subscription_plan, country y favorite_genre
3. Eliminación de valores imposibles en age y customer_support_tickets
4. Imputación de nulos en monthly_watch_time_mins con la mediana
5. Eliminación de fechas inválidas en last_login_date
""")