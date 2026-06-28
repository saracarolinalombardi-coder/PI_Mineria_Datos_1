import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import os

# Cargamos el dataset limpio
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
df = pd.read_csv(os.path.join(BASE_DIR, 'data', 'processed', 'streaming_users_clean.csv'))

st.title("Escalamiento y PCA")

st.markdown("### Variables utilizadas")
st.write("""
Para aplicar PCA se seleccionaron las tres variables numéricas continuas del dataset:
age, monthly_watch_time_mins y customer_support_tickets.
Las variables categóricas se excluyen porque PCA requiere datos numéricos.
""")

st.markdown("### Escalas originales")
variables = ['age', 'monthly_watch_time_mins', 'customer_support_tickets']
X = df[variables]
st.dataframe(X.describe().round(2))

st.markdown("### Escalamiento aplicado")
st.write("""
Las variables presentan escalas muy distintas entre sí: monthly_watch_time_mins
tiene valores de hasta 2704 minutos mientras que customer_support_tickets varía
entre 0 y 4. Sin escalar, monthly_watch_time_mins dominaría artificialmente
la dirección de máxima varianza por razones puramente numéricas.
Se aplica estandarización Z-score (StandardScaler) que lleva todas las variables
a media 0 y desviación estándar 1.
""")

# Escalamiento
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA completo
pca_full = PCA()
pca_full.fit(X_scaled)

varianza = pca_full.explained_variance_ratio_
acumulada = varianza.cumsum()

st.markdown("### Varianza explicada por componente")
for i in range(len(varianza)):
    st.write(f"PC{i+1}: {varianza[i]*100:.2f}% | Varianza acumulada: {acumulada[i]*100:.2f}%")

# --- VISUALIZACIÓN 1: Scree plot ---
st.markdown("### Visualización 1 - Scree plot")

fig1, ax1 = plt.subplots(figsize=(8, 5))
ax1.bar(range(1, len(varianza)+1), varianza*100,
        color='steelblue', edgecolor='white', label='Varianza por componente')
ax1.plot(range(1, len(varianza)+1), acumulada*100,
         'o-', color='coral', linewidth=2, label='Varianza acumulada')
ax1.axhline(y=80, color='gray', linestyle='--', alpha=0.7, label='Umbral 80%')
ax1.axhline(y=95, color='green', linestyle='--', alpha=0.7, label='Umbral 95%')
ax1.set_xlabel('Componente principal')
ax1.set_ylabel('Varianza explicada (%)')
ax1.set_title('Scree plot — Varianza explicada por componente')
ax1.legend()
st.pyplot(fig1)

st.write("""
La varianza se distribuye de forma casi uniforme entre los tres componentes
(aproximadamente 33% cada uno). Esto indica que las tres variables numéricas
aportan información independiente y no redundante entre sí, lo cual es
coherente con las bajas correlaciones observadas en el EDA.
Para superar el umbral del 80% de varianza acumulada se necesitan las tres
componentes, lo que confirma que no es posible reducir dimensiones sin
pérdida significativa de información en este dataset.
""")

# Proyección a 2 componentes
pca_2d = PCA(n_components=2)
X_pca = pca_2d.fit_transform(X_scaled)

# Loadings
loadings = pd.DataFrame(
    pca_2d.components_.T,
    index=variables,
    columns=['PC1', 'PC2']
).round(3)

st.markdown("### Loadings")
st.dataframe(loadings)

# --- VISUALIZACIÓN 2: Proyección ---
st.markdown("### Visualización 2 - Proyección de usuarios en PC1 y PC2")

df_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
df_pca['subscription_plan'] = df['subscription_plan'].values

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.scatterplot(
    data=df_pca, x='PC1', y='PC2',
    hue='subscription_plan', palette='Set2',
    alpha=0.5, s=20, ax=ax2
)
ax2.set_xlabel(f"PC1 ({pca_2d.explained_variance_ratio_[0]*100:.1f}% varianza)")
ax2.set_ylabel(f"PC2 ({pca_2d.explained_variance_ratio_[1]*100:.1f}% varianza)")
ax2.set_title('Proyección de usuarios en PC1 y PC2')
st.pyplot(fig2)

st.write("""
La proyección muestra que los usuarios no forman grupos claramente
diferenciados en el espacio de las dos primeras componentes.
Esto es consistente con la distribución uniforme de varianza y
con la ausencia de correlaciones fuertes entre las variables originales.

PC1 recibe contribuciones similares de las tres variables, con mayor
peso en customer_support_tickets. PC2 opone age contra
monthly_watch_time_mins, capturando la diferencia entre usuarios
mayores con menor consumo y usuarios jóvenes con mayor consumo.

Limitación: con solo 3 variables numéricas la varianza se distribuye
uniformemente entre los 3 componentes. Para superar el 80% de varianza
acumulada se necesitan las 3 componentes originales.
""")