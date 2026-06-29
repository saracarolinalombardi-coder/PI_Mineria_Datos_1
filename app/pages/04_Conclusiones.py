import streamlit as st

st.title("Conclusiones")

st.markdown("### Resultados del análisis")

st.write("""
**Calidad de datos:** Después de limpiar el dataset, logramos conservar el 96.6% de los registros (7.884 de 8.160). Los principales problemas fueron valores nulos, duplicados, edades imposibles y categorías mal escritas.

**Plan de suscripción vs tiempo de visualización:** No encontramos diferencias significativas entre los planes Básico, Estándar y Premium. Todos los usuarios ven cantidades similares de contenido.

**Edad vs consumo:** La edad no está relacionada con el tiempo de visualización. Personas de distintas edades tienen comportamientos de consumo parecidos.

**Tickets de soporte vs consumo:** Los usuarios que reportan más problemas técnicos no ven menos contenido. No hay relación entre estas variables.

**Reducción de dimensionalidad:** Con PCA vimos que las tres variables numéricas (edad, tiempo, tickets) son independientes entre sí. No se puede reducir el número de variables sin perder información valiosa.
""")

st.markdown("### ¿Qué podemos mejorar?")

st.write("""
Para futuros análisis, sería útil agregar más información sobre los usuarios, como:
- Frecuencia de acceso a la plataforma
- Tipo de contenido preferido (series, películas, documentales)
- Dispositivo desde el que se conectan

También se podrían aplicar técnicas de segmentación para agrupar usuarios con comportamientos similares y estudiar la evolución de sus hábitos en el tiempo.
""")

st.markdown("---")
st.markdown("[Ver repositorio en GitHub](https://github.com/saracarolinalombardi-coder/PI_Mineria_Datos_1)")