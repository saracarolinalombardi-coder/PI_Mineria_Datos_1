import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import os

# ---------- CARGA DE DATOS ----------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@st.cache_data
def cargar_datos():
    return pd.read_csv(os.path.join(BASE_DIR, 'data', 'processed', 'streaming_users_clean.csv'))

df = cargar_datos()

st.title("Escalamiento y PCA")
st.caption("Cada gráfico responde una pregunta y lleva su interpretación.")

# ---------- VARIABLES ----------
st.subheader("Variables utilizadas")
st.markdown("""
Para aplicar PCA se seleccionaron las tres variables numéricas continuas del dataset:
age, monthly_watch_time_mins y customer_support_tickets.
Las variables categóricas se excluyen porque PCA requiere datos numéricos.
""")

variables = ['age', 'monthly_watch_time_mins', 'customer_support_tickets']
X = df[variables]

# ---------- ESCALAS ORIGINALES ----------
st.subheader("Escalas originales")
st.dataframe(X.describe().round(2))

# ---------- ESCALAMIENTO ----------
st.subheader("Escalamiento aplicado")
st.markdown("""
**Interpretación:** Las variables presentan escalas muy distintas entre sí: monthly_watch_time_mins
tiene valores de hasta 2704 minutos mientras que customer_support_tickets varía
entre 0 y 4. Sin escalar, monthly_watch_time_mins dominaría artificialmente
la dirección de máxima varianza por razones puramente numéricas.
Se aplica estandarización Z-score (StandardScaler) que lleva todas las variables
a media 0 y desviación estándar 1.
""")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ---------- PCA COMPLETO ----------
pca_full = PCA()
pca_full.fit(X_scaled)

varianza = pca_full.explained_variance_ratio_
acumulada = varianza.cumsum()

st.subheader("Varianza explicada por componente")
for i in range(len(varianza)):
    st.write(f"PC{i+1}: {varianza[i]*100:.2f}% | Varianza acumulada: {acumulada[i]*100:.2f}%")

# ---------- VISUALIZACIÓN 1: Scree plot ----------
st.subheader("1. Scree plot")

componentes = [f"PC{i+1}" for i in range(len(varianza))]

fig1 = go.Figure()
fig1.add_trace(go.Bar(
    x=componentes, y=varianza * 100,
    name='Varianza por componente',
    marker_color='steelblue', marker_line_color='white', marker_line_width=1
))
fig1.add_trace(go.Scatter(
    x=componentes, y=acumulada * 100,
    mode='lines+markers', name='Varianza acumulada',
    line=dict(color='coral', width=2), marker=dict(size=8)
))
fig1.add_hline(y=80, line_dash='dash', line_color='gray',
               annotation_text='Umbral 80%', annotation_position='bottom right')
fig1.add_hline(y=95, line_dash='dash', line_color='green',
               annotation_text='Umbral 95%', annotation_position='bottom right')
fig1.update_layout(
    xaxis_title='Componente principal',
    yaxis_title='Varianza explicada (%)',
    title='Scree plot — Varianza explicada por componente',
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
)
st.plotly_chart(fig1, use_container_width=True)

st.markdown("""
**Interpretación:** La varianza se distribuye de forma casi uniforme entre los tres componentes
(aproximadamente 33% cada uno). Esto indica que las tres variables numéricas
aportan información independiente y no redundante entre sí, lo cual es
coherente con las bajas correlaciones observadas en el EDA.
Para superar el umbral del 80% de varianza acumulada se necesitan las tres
componentes, lo que confirma que no es posible reducir dimensiones sin
pérdida significativa de información en este dataset.
""")

# ---------- PROYECCIÓN 2D ----------
pca_2d = PCA(n_components=2)
X_pca = pca_2d.fit_transform(X_scaled)

loadings = pd.DataFrame(
    pca_2d.components_.T,
    index=variables,
    columns=['PC1', 'PC2']
).round(3)

st.subheader("Loadings")
st.dataframe(loadings)

# ---------- VISUALIZACIÓN 2: Proyección ----------
st.subheader("2. Proyección de usuarios en PC1 y PC2")

df_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
df_pca['subscription_plan'] = df['subscription_plan'].values

fig2 = px.scatter(
    df_pca, x='PC1', y='PC2',
    color='subscription_plan',
    opacity=0.5,
    labels={
        'PC1': f"PC1 ({pca_2d.explained_variance_ratio_[0]*100:.1f}% varianza)",
        'PC2': f"PC2 ({pca_2d.explained_variance_ratio_[1]*100:.1f}% varianza)",
        'subscription_plan': 'Plan'
    }
)
fig2.update_traces(marker=dict(size=4))
fig2.update_layout(title='Proyección de usuarios en PC1 y PC2')
st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
**Interpretación:** La proyección muestra que los usuarios no forman grupos claramente
diferenciados en el espacio de las dos primeras componentes.
Esto es consistente con la distribución uniforme de varianza y
con la ausencia de correlaciones fuertes entre las variables originales.

PC1 recibe contribuciones similares de las tres variables, con mayor
peso en customer_support_tickets. PC2 opone age contra
monthly_watch_time_mins, capturando la diferencia entre usuarios
mayores con menor consumo y usuarios jóvenes con mayor consumo.

**Limitación:** con solo 3 variables numéricas la varianza se distribuye
uniformemente entre los 3 componentes. Para superar el 80% de varianza
acumulada se necesitan las 3 componentes originales.
""")