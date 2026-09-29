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
   if (6.0 <= pH <= 7.0):
       resultado = "Lote aprobado"
   elif (20 <= temperatura <= 25):
       resultado = "Lote aprobado"
   else:
       resultado = "Lote no aprobado"      
    st.write(f"Resultado: {resultado}")
