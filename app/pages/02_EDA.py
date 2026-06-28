import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ---------- CARGA DE DATOS ----------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@st.cache_data
def cargar_datos():
    return pd.read_csv(os.path.join(BASE_DIR, 'data', 'processed', 'streaming_users_clean.csv'))

df = cargar_datos()
orden_plan = ['Básico', 'Estándar', 'Premium']

st.title("Análisis Exploratorio de Datos")
st.caption("Cada gráfico responde una pregunta y lleva su interpretación.")

# ---------- VISUALIZACIÓN 1 ----------
st.subheader("1. Distribución de edades")
fig1 = px.histogram(df, x='age', nbins=20,
                    color_discrete_sequence=['steelblue'],
                    labels={'age': 'Edad'})
fig1.update_traces(marker_line_color='white', marker_line_width=1)
fig1.update_layout(xaxis_title='Edad', yaxis_title='Cantidad de usuarios',
                   title='Distribución de edades de los usuarios')
st.plotly_chart(fig1, use_container_width=True)
st.markdown("""
**Interpretación:** La distribución de edades se concentra entre los 20 y 50 años, con mayor
frecuencia en la franja de 25 a 40 años. Esto indica que la plataforma
tiene mayor adopción entre adultos jóvenes y de mediana edad.
""")

# ---------- VISUALIZACIÓN 2 ----------
st.subheader("2. Tiempo mensual de visualización")
fig2 = px.histogram(df, x='monthly_watch_time_mins', nbins=30,
                    color_discrete_sequence=['coral'],
                    labels={'monthly_watch_time_mins': 'Minutos por mes'})
fig2.update_traces(marker_line_color='white', marker_line_width=1)
fig2.update_layout(xaxis_title='Minutos por mes', yaxis_title='Cantidad de usuarios',
                   title='Distribución del tiempo mensual de visualización')
st.plotly_chart(fig2, use_container_width=True)
st.markdown("""
**Interpretación:** El tiempo de visualización se distribuye de forma aproximadamente simétrica,
con la mayoría de los usuarios entre 400 y 1200 minutos mensuales.
Este resultado es el punto de partida para analizar si el plan de suscripción
influye en el tiempo de consumo.
""")

# ---------- VISUALIZACIÓN 3 ----------
st.subheader("3. Tiempo de visualización por plan")
fig3 = px.box(df, x='subscription_plan', y='monthly_watch_time_mins',
              color='subscription_plan',
              category_orders={'subscription_plan': orden_plan},
              labels={'subscription_plan': 'Plan de suscripción',
                      'monthly_watch_time_mins': 'Minutos por mes'})
fig3.update_layout(title='Tiempo de visualización mensual por plan de suscripción')
st.plotly_chart(fig3, use_container_width=True)
st.markdown("""
**Interpretación:** Los tres planes muestran distribuciones similares de tiempo de visualización,
sin diferencias marcadas entre ellos. Esto sugiere que el plan contratado
no determina cuánto consume el usuario mensualmente.
""")

# ---------- VISUALIZACIÓN 4 ----------
st.subheader("4. Tickets de soporte por país")
tickets_pais = df.groupby('country')['customer_support_tickets'].mean().sort_values(ascending=False)
fig4 = px.bar(x=tickets_pais.index, y=tickets_pais.values,
              color_discrete_sequence=['mediumpurple'],
              labels={'x': 'País', 'y': 'Promedio de tickets'})
fig4.update_traces(marker_line_color='white', marker_line_width=1)
fig4.update_layout(title='Promedio de tickets de soporte por país',
                   xaxis_tickangle=-45)
st.plotly_chart(fig4, use_container_width=True)
st.markdown("""
**Interpretación:** El promedio de tickets varía entre países, lo que podría indicar diferencias
en la experiencia del usuario según la región. Los países con mayor promedio
podrían estar experimentando problemas técnicos más frecuentes.
""")

# ---------- VISUALIZACIÓN 5 ----------
st.subheader("5. Mapa de correlaciones")
variables_numericas = df[['age', 'monthly_watch_time_mins', 'customer_support_tickets']]
corr = variables_numericas.corr()
fig5 = px.imshow(corr, text_auto='.2f', color_continuous_scale='RdBu_r',
                 zmin=-1, zmax=1,
                 labels={'color': 'Correlación'})
fig5.update_layout(title='Mapa de calor de correlaciones entre variables numéricas')
st.plotly_chart(fig5, use_container_width=True)
st.markdown("""
**Interpretación:** Las variables numéricas no presentan correlaciones fuertes entre sí,
lo que indica que cada una aporta información independiente. La correlación
cercana a cero entre tickets y tiempo de visualización sugiere que los
usuarios continúan consumiendo contenido a pesar de reportar incidencias.
""")