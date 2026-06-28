import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Cargamos el dataset limpio
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
df = pd.read_csv(os.path.join(BASE_DIR, 'data', 'processed', 'streaming_users_clean.csv'))
st.title("Escalamiento y PCA")

st.markdown("### Variables utilizadas")
st.write("""
Se seleccionaron las tres variables numéricas continuas del dataset:
age, monthly_watch_time_mins y customer_support_tickets.
Se excluyeron las variables categóricas porque PCA requiere variables numéricas.
""")

st.markdown("### Escalamiento aplicado")
st.write("""
Se aplicó estandarización Z-score (StandardScaler) antes del PCA.
Sin escalamiento, la variable con mayor varianza dominaría los componentes
sin ninguna razón válida. Tras estandarizar, todas las variables
contribuyen de forma equitativa.
""")

# Aplicamos escalamiento y PCA
variables = ['age', 'monthly_watch_time_mins', 'customer_support_tickets']
X = df[variables]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=3)
pca.fit(X_scaled)

varianza_explicada = pca.explained_variance_ratio_
varianza_acumulada = varianza_explicada.cumsum()

# --- VISUALIZACIÓN 1 -----
st.markdown("### Varianza explicada por componente")

fig1, ax1 = plt.subplots(figsize=(8, 5))
ax1.bar(range(1, 4), varianza_explicada * 100, color='steelblue',
        edgecolor='white', label='Varianza por componente')
ax1.plot(range(1, 4), varianza_acumulada * 100, 'o-',
         color='coral', linewidth=2, label='Varianza acumulada')
ax1.axhline(y=80, color='gray', linestyle='--', alpha=0.7, label='Umbral 80%')
ax1.set_xlabel('Componente principal')
ax1.set_ylabel('Varianza explicada (%)')
ax1.set_title('Varianza explicada por componente principal')
ax1.legend()
st.pyplot(fig1)

st.write("""
PC1 explica el 33.7%, PC2 el 33.2% y PC3 el 33.0% de la varianza.
La distribución uniforme indica que ninguna componente captura
una proporción dominante, lo cual es coherente con las bajas
correlaciones entre variables.
""")

# --- VISUALIZACIÓN 2 ---
st.markdown("### Proyección de usuarios en PC1 y PC2")

X_pca = pca.transform(X_scaled)

fig2, ax2 = plt.subplots(figsize=(10, 6))
scatter = ax2.scatter(X_pca[:, 0], X_pca[:, 1],
                      c=df['monthly_watch_time_mins'],
                      cmap='coolwarm', alpha=0.4, s=10)
plt.colorbar(scatter, label='Tiempo de visualización (min)')
ax2.set_xlabel('Componente Principal 1')
ax2.set_ylabel('Componente Principal 2')
ax2.set_title('Proyección de usuarios en PC1 y PC2')
st.pyplot(fig2)

st.write("""
La proyección muestra que los usuarios no forman grupos claramente
diferenciados en el espacio de las dos primeras componentes.
Esto es consistente con la distribución uniforme de varianza y
con la ausencia de correlaciones fuertes entre las variables originales.
""")

# --- LOADINGS ---
st.markdown("### Interpretación de las componentes")

loadings = pd.DataFrame(
    pca.components_.T,
    index=variables,
    columns=['PC1', 'PC2', 'PC3']
).round(3)

st.dataframe(loadings)

st.write("""
PC1 combina las tres variables con pesos similares, representando
un perfil general del usuario. PC2 opone edad contra tiempo de
visualización, capturando la diferencia entre usuarios mayores
con menor consumo y jóvenes con mayor consumo. PC3 representa
el nivel de incidencias técnicas de forma aislada.
""")