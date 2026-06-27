import streamlit as st

st.title("Conclusiones")

st.markdown("### Hallazgos principales")
st.write("""
- El dataset original presentó problemas significativos de calidad que
  requirieron un proceso de limpieza documentado. Tras el proceso se
  retuvo el 72.1% de los registros originales.
- El plan de suscripción no es un factor determinante del tiempo de
  visualización mensual del usuario.
- La edad no presenta una relación lineal con el tiempo de consumo,
  lo que indica que usuarios de distintas edades tienen comportamientos
  similares.
- Los usuarios que generan más tickets de soporte no consumen
  significativamente menos contenido, lo que sugiere que las incidencias
  técnicas no afectan el tiempo de uso.
- El PCA confirmó que las tres variables numéricas aportan información
  independiente y no redundante al dataset.
""")

st.markdown("### Limitaciones")
st.write("""
- El alcance de las conclusiones está condicionado por la calidad inicial
  del dataset y por las decisiones de limpieza documentadas. La eliminación
  del 27.9% de los registros puede haber afectado la representatividad
  de algunos grupos.
- Las variables disponibles son limitadas para explicar el comportamiento
  de consumo: no se cuenta con información sobre dispositivo, historial
  de contenido o frecuencia de acceso.
- Las correlaciones analizadas son lineales; podrían existir relaciones
  no lineales que este análisis no captura.
""")

st.markdown("### Próximos pasos")
st.write("""
- Incorporar variables adicionales como frecuencia de acceso o tipo de
  contenido consumido para ampliar el análisis de comportamiento.
- Aplicar técnicas de segmentación como clustering para identificar
  grupos de usuarios con perfiles similares.
- Analizar la evolución temporal del comportamiento de los usuarios
  a partir de la variable last_login_date para estudiar patrones
  de retención en la plataforma.
""")

st.markdown("---")
st.markdown("### Enlaces")
st.markdown("[Ver repositorio en GitHub](https://github.com/saracarolinalombardi-coder/PI_Mineria_Datos_1)")