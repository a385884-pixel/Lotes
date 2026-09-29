import streamlit as st

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

   if 6.0 <=ph <= and 20.0 <=temperatura <=25.0:
      resultado = "Lote aprobado"
   else:
       resultado = "Lote no aprobado"
       
    st.write(f"Resultado: {resultado}")
