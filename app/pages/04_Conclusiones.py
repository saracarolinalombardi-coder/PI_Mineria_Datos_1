import streamlit as st

st.title("Conclusiones del Análisis")

st.markdown("### Hallazgos principales")

st.write("""
El proceso de limpieza permitió conservar el 96.6% de los registros originales, pasando de 8.160 a 7.884 filas útiles para el análisis.

El plan de suscripción no mostró incidencia en el tiempo de visualización mensual. Los usuarios de los tres planes (Básico, Estándar y Premium) presentan comportamientos de consumo similares, con medianas cercanas a los 760 minutos mensuales.

No se encontró relación entre la edad y el tiempo de consumo (correlación de 0.01), ni entre los tickets de soporte y el tiempo de visualización (correlación de 0.00). Estas variables no explican el comportamiento de los usuarios en la plataforma.

El análisis de componentes principales confirmó que las tres variables numéricas disponibles son independientes entre sí, cada una explicando aproximadamente un tercio de la varianza total. No fue posible reducir la dimensionalidad sin pérdida significativa de información.
""")

st.markdown("### Interpretación de los resultados")

st.write("""
Los resultados muestran que ni la edad, ni el plan de suscripción, ni los tickets de soporte explican el tiempo de consumo de los usuarios.

Esto sugiere que el comportamiento en la plataforma responde a otros factores no considerados en este análisis, como preferencias de contenido o hábitos de consumo.

La ausencia de relaciones significativas entre las variables también plantea un interrogante sobre la naturaleza del dataset, que parece carecer de los patrones típicamente esperados en datos reales de consumo.
""")

st.markdown("### Limitaciones identificadas")

st.write("""
- La imputación de valores nulos con la mediana pudo haber aplanado diferencias entre usuarios.
- El análisis se limitó a relaciones lineales, dejando fuera posibles patrones no lineales.
- La cantidad de variables numéricas (solo 3) es reducida para aplicar PCA con resultados significativos.
- No se cuenta con información sobre frecuencia de acceso, tipo de contenido consumido o dispositivo de conexión.
""")

st.markdown("---")
st.markdown("### 📎 Enlaces")
st.markdown("[Repositorio en GitHub](https://github.com/saracarolinalombardi-coder/PI_Mineria_Datos_1)")