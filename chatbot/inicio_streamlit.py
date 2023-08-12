import streamlit as st

st.title("Meu primeiro app")

st.header("teste de cabeçalho")
st.subheader("teste de subcabeçalho")
st.write("funcao escrita")

var = st.text_input("Digite algo aqui: ")
st.write(var)