import streamlit as st

st.sidebar.title("Actividad 7")
st.sidebar.write("Valeria Fernandez Castillo, 3L, FCQ")

st.title("Evaluación de un lote")

pH = st.number_input(
    "pH",
    value=6.5
)

temperatura = st.number_input(
    "Temperatura (°C)",
    value=23.0
)

if st.button("Evaluar"):
   if ph >= 60 and temperatura >= 20:
       resultado = "Lote aprobado"
   elif ph <= 70 and temperatura <=25:
       resultado = "Lote aprobado"
   else:
       resultado = "Lote no aprobado"      
    st.write(f"Resultado: {resultado}")
