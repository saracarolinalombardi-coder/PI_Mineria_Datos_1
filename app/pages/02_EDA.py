import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargamos el dataset limpio
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
df = pd.read_csv(os.path.join(BASE_DIR, 'data', 'processed', 'streaming_users_clean.csv'))
st.title("Análisis Exploratorio de Datos")

# --- VISUALIZACIÓN 1 ---
st.markdown("### Visualización 1 - Distribución de edades")

fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.histplot(df['age'], bins=20, color='steelblue', edgecolor='white', ax=ax1)
ax1.set_xlabel('Edad')
ax1.set_ylabel('Cantidad de usuarios')
ax1.set_title('Distribución de edades de los usuarios')
st.pyplot(fig1)

st.write("""
La distribución de edades se concentra entre los 20 y 50 años, con mayor
frecuencia en la franja de 25 a 40 años. Esto indica que la plataforma
tiene mayor adopción entre adultos jóvenes y de mediana edad.
""")

# --- VISUALIZACIÓN 2 ---
st.markdown("### Visualización 2 - Tiempo mensual de visualización")

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.histplot(df['monthly_watch_time_mins'], bins=30, color='coral',
             edgecolor='white', ax=ax2)
ax2.set_xlabel('Minutos por mes')
ax2.set_ylabel('Cantidad de usuarios')
ax2.set_title('Distribución del tiempo mensual de visualización')
st.pyplot(fig2)

st.write("""
El tiempo de visualización se distribuye de forma aproximadamente simétrica,
con la mayoría de los usuarios entre 400 y 1200 minutos mensuales.
Este resultado es el punto de partida para analizar si el plan de suscripción
influye en el tiempo de consumo.
""")

# --- VISUALIZACIÓN 3 ---
st.markdown("### Visualización 3 - Tiempo de visualización por plan")

fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df, x='subscription_plan', y='monthly_watch_time_mins',
            palette='Set2', order=['Básico', 'Estándar', 'Premium'], ax=ax3)
ax3.set_xlabel('Plan de suscripción')
ax3.set_ylabel('Minutos por mes')
ax3.set_title('Tiempo de visualización mensual por plan de suscripción')
st.pyplot(fig3)

st.write("""
Los tres planes muestran distribuciones similares de tiempo de visualización,
sin diferencias marcadas entre ellos. Esto sugiere que el plan contratado
no determina cuánto consume el usuario mensualmente.
""")

# --- VISUALIZACIÓN 4 ---
st.markdown("### Visualización 4 - Tickets de soporte por país")

tickets_pais = df.groupby('country')['customer_support_tickets'].mean().sort_values(ascending=False)

fig4, ax4 = plt.subplots(figsize=(10, 5))
tickets_pais.plot(kind='bar', color='mediumpurple', edgecolor='white', ax=ax4)
ax4.set_xlabel('País')
ax4.set_ylabel('Promedio de tickets')
ax4.set_title('Promedio de tickets de soporte por país')
plt.xticks(rotation=45)
st.pyplot(fig4)

st.write("""
El promedio de tickets varía entre países, lo que podría indicar diferencias
en la experiencia del usuario según la región. Los países con mayor promedio
podrían estar experimentando problemas técnicos más frecuentes.
""")

# --- VISUALIZACIÓN 5 ---
st.markdown("### Visualización 5 - Mapa de correlaciones")

variables_numericas = df[['age', 'monthly_watch_time_mins', 'customer_support_tickets']]

fig5, ax5 = plt.subplots(figsize=(8, 6))
sns.heatmap(variables_numericas.corr(), annot=True, fmt='.2f',
            cmap='coolwarm', center=0, linewidths=0.5, ax=ax5)
ax5.set_title('Mapa de calor de correlaciones entre variables numéricas')
st.pyplot(fig5)

st.write("""
Las variables numéricas no presentan correlaciones fuertes entre sí,
lo que indica que cada una aporta información independiente. La correlación
cercana a cero entre tickets y tiempo de visualización sugiere que los
usuarios continúan consumiendo contenido a pesar de reportar incidencias.
""")