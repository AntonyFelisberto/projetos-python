import streamlit as st

st.title("Meu segundo app")

st.sidebar.title("Configuracoes")

st.sidebar.write("Nome usuario")
nome = st.sidebar.text_input("Digite seu nome: ")

st.header("Nome do usuario: ")
st.subheader(nome)

st.sidebar.subheader("Numeros: ")
primeiro = st.sidebar.number_input("Digite o primeiro numero: ")
segundo = st.sidebar.number_input("Digite o segundo numero: ")

st.sidebar.subheader("Operacao")
operacao = st.sidebar.radio("Escolha a operação:",("Adicao","Subtracao"))

btn_calc = st.button("Calcular")
if btn_calc:
    st.header("Operacao Escolhida")
    st.subheader(operacao)
    st.header("numeros selecionados")
    st.subheader(f"o primeiro foi {primeiro} e o segundo foi {segundo}")
    st.header("resultado operacao")
    if operacao=="Adicao":
        resultado = primeiro + segundo
    else:
        resultado = primeiro - segundo
    st.subheader(f"o resultado operacao foi {resultado}")
    st.write("usando streamlit")

if "nome_usuario" not in st.session_state:
        #st.session_state['nome_usuario']
        st.session_state.nome_usuario

nome = st.text_input("Digite o nome do usuario: ")
st.session_state.nome_usuario.append(nome)    