import random
import streamlit as st

# Configuração da página para celular e PC
st.set_page_config(page_title="Desafio de Matemática", page_icon="🧠")

st.title("🎮 Desafio de Matemática")
st.write("Responda as perguntas e teste seus conhecimentos!")

# Inicializa as variáveis no histórico da sessão (para não perder os pontos)
if "pontos" not in st.session_state:
    st.session_state.pontos = 0
if "num1" not in st.session_state:
    st.session_state.num1 = random.randint(1, 10)
if "num2" not in st.session_state:
    st.session_state.num2 = random.randint(1, 10)
if "operacao" not in st.session_state:
    st.session_state.operacao = "+"


def nova_pergunta():
    """Gera novos números para a próxima conta"""
    st.session_state.num1 = random.randint(1, 10)
    st.session_state.num2 = random.randint(1, 10)
    st.session_state.operacao = random.choice(["+", "-", "*"])

    # Evita conta negativa na subtração
    if (
        st.session_state.operacao == "-"
        and st.session_state.num1 < st.session_state.num2
    ):
        st.session_state.num1, st.session_state.num2 = (
            st.session_state.num2,
            st.session_state.num1,
        )


# Mostra a pontuação
st.metric(label="Pontuação Atual", value=st.session_state.pontos)

# Exibe a pergunta
n1 = st.session_state.num1
n2 = st.session_state.num2
op = st.session_state.operacao
sinal = "x" if op == "*" else op

st.subheader(f"Quanto é {n1} {sinal} {n2}?")

# Campo para o usuário digitar no celular
resposta = st.number_input(
    "Sua resposta:", step=1, value=None, key="input_resposta"
)

# Botão de enviar
if st.button("Enviar Resposta", type="primary"):
    if resposta is not None:
        # Calcula o resultado esperado
        if op == "+":
            correto = n1 + n2
        elif op == "-":
            correto = n1 - n2
        else:
            correto = n1 * n2

        if int(resposta) == correto:
            st.success("✨ Parabéns! Você acertou (+10 pontos)")
            st.session_state.pontos += 10
            nova_pergunta()
            st.rerun()
        else:
            st.error(f"❌ Errou! A resposta correta era {correto}.")
            nova_pergunta()
            st.rerun()
    else:
        st.warning("⚠️ Digite um número antes de enviar!")