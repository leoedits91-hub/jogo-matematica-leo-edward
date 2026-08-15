import random
import streamlit as st

st.set_page_config(
    page_title="Quiz de Estudos - 3º Ano", page_icon="📚", layout="centered"
)

# Banco de dados de perguntas com explicações detalhadas
BANCO_PERGUNTAS = {
    "Educação Física (Danças)": [
        {
            "pergunta": "Qual destas danças é considerada uma dança folclórica e de roda muito tradicional no Brasil?",
            "opcoes": ["Ciranda", "Hip-hop", "Ballet clássico", "Tango"],
            "correta": "Ciranda",
            "explicacao": "A Ciranda é uma dança comunitária de roda típica do Brasil (muito forte em Pernambuco), onde todos se dão as mãos, simbolizando união e integração social.",
        },
        {
            "pergunta": "Qual elemento da dança está relacionado ao uso do ritmo, da velocidade e das pausas nos movimentos?",
            "opcoes": ["Tempo", "Espaço", "Peso do corpo", "Figurino"],
            "correta": "Tempo",
            "explicacao": "O elemento 'Tempo' diz respeito ao ritmo da música, à velocidade da execução (rápido ou lento) e às pausas feitas durante a dança.",
        },
        {
            "pergunta": "A dança Frevo, conhecida pelo uso de pequenos guarda-chuvas coloridos, é originária de qual estado brasileiro?",
            "opcoes": [
                "Pernambuco",
                "Rio de Janeiro",
                "Rio Grande do Sul",
                "Bahia",
            ],
            "correta": "Pernambuco",
            "explicacao": "O Frevo nasceu no estado de Pernambuco. Ele combina ritmos acelerados, passos de capoeira e o famoso guarda-chuva colorido para dar equilíbrio ao passista.",
        },
        {
            "pergunta": "O que caracteriza a dança de rua (Street Dance/Hip-hop)?",
            "opcoes": [
                "Surgir em espaços urbanos com movimentos fortes e improvisação",
                "Ser dançada apenas em palcos com sapatilhas de ponta",
                "O uso de roupas de época e ritmo de valsa lenta",
                "Falta total de ritmo ou acompanhamento musical",
            ],
            "correta": (
                "Surgir em espaços urbanos com movimentos fortes e"
                " improvisação"
            ),
            "explicacao": "As danças urbanas surgiram nos centros das grandes cidades como forma de expressão cultural e artística dos jovens, usando improvisação e movimentos marcados.",
        },
    ],
    "Geografia (3º Ano - 3º Bimestre)": [
        {
            "pergunta": "Qual é a principal diferença entre a área urbana (cidade) e a área rural (campo)?",
            "opcoes": [
                "A área urbana possui mais construções e serviços; a rural foca na agricultura e natureza",
                "A área rural tem mais prédios e avenidas do que a urbana",
                "A área urbana produz alimentos agrícolas para todo o país sozinha",
                "Não existe diferença entre o campo e a cidade",
            ],
            "correta": (
                "A área urbana possui mais construções e serviços; a rural foca"
                " na agricultura e natureza"
            ),
            "explicacao": "O espaço urbano concentra comércios, indústrias e serviços densos. O espaço rural foca em atividades do setor primário, como agricultura, pecuária e preservação da natureza.",
        },
        {
            "pergunta": "Como o campo e a cidade se ajudam no dia a dia (interdependência)?",
            "opcoes": [
                "O campo envia alimentos/matérias-primas e a cidade fornece produtos industrializados e serviços",
                "A cidade envia plantas para o campo produzir máquinas pesadas",
                "O campo não precisa de nenhum produto fabricado na cidade",
                "A cidade produz todas as suas frutas e vegetais dentro dos apartamentos",
            ],
            "correta": (
                "O campo envia alimentos/matérias-primas e a cidade fornece"
                " produtos industrializados e serviços"
            ),
            "explicacao": "Há uma relação de troca: o campo fornece matérias-primas e alimentos essenciais para a cidade, enquanto a cidade produz tecnologias, adubos, máquinas e serviços utilizados no campo.",
        },
        {
            "pergunta": "Qual das opções descreve uma transformação da paisagem causada pela ação humana (cultural)?",
            "opcoes": [
                "Construção de uma ponte sobre um rio",
                "Erupção de um vulcão natural",
                "Crescimento natural de uma floresta intocada",
                "Desgastamento das rochas pela força da chuva",
            ],
            "correta": "Construção de uma ponte sobre um rio",
            "explicacao": "Paisagens culturais ou modificadas são aquelas alteradas pela intervenção do ser humano (como estradas, pontes e prédios), ao contrário das paisagens puramente naturais.",
        },
        {
            "pergunta": "O que é matéria-prima?",
            "opcoes": [
                "O material bruto retirado da natureza usado para fabricar produtos",
                "O produto final vendido na prateleira do supermercado",
                "O dinheiro usado para comprar máquinas industriais",
                "O lixo descartado pelas grandes fábricas",
            ],
            "correta": (
                "O material bruto retirado da natureza usado para fabricar"
                " produtos"
            ),
            "explicacao": "Matéria-prima é o elemento natural bruto (como o leite, o algodão ou a madeira) que é transformado pelas indústrias em produtos finais (como queijo, roupas ou móveis).",
        },
    ],
}

TOTAL_PERGUNTAS_POR_JOGO = 4

# Estado da sessão
if "pontos" not in st.session_state:
    st.session_state.pontos = 0
if "pergunta_atual_idx" not in st.session_state:
    st.session_state.pergunta_atual_idx = 0
if "perguntas_sorteadas" not in st.session_state:
    st.session_state.perguntas_sorteadas = []
if "tema_escolhido" not in st.session_state:
    st.session_state.tema_escolhido = None
if "respondido" not in st.session_state:
    st.session_state.respondido = False
if "resposta_correta_flag" not in st.session_state:
    st.session_state.resposta_correta_flag = False


def reiniciar_jogo():
    st.session_state.pontos = 0
    st.session_state.pergunta_atual_idx = 0
    st.session_state.perguntas_sorteadas = []
    st.session_state.tema_escolhido = None
    st.session_state.respondido = False
    st.session_state.resposta_correta_flag = False


st.title("🎯 Quiz Interativo de Estudos")

# Tela 1: Escolha de Tema
if st.session_state.tema_escolhido is None:
    st.write("Escolha a matéria que deseja praticar hoje:")
    tema = st.radio("Selecione o tema:", list(BANCO_PERGUNTAS.keys()))
    if st.button("Iniciar Quiz", type="primary"):
        st.session_state.tema_escolhido = tema
        lista_perguntas = BANCO_PERGUNTAS[tema].copy()
        random.shuffle(lista_perguntas)
        st.session_state.perguntas_sorteadas = lista_perguntas[
            :TOTAL_PERGUNTAS_POR_JOGO
        ]
        st.rerun()

# Tela 2: Fim do Quiz
elif (
    st.session_state.pergunta_atual_idx >= len(st.session_state.perguntas_sorteadas)
):
    st.balloons()
    st.header("🏆 Quiz Concluído!")
    total = len(st.session_state.perguntas_sorteadas)
    pontos = st.session_state.pontos
    st.subheader(f"Sua pontuação final: {pontos} de {total} acertos.")

    if pontos == total:
        st.success("Excelente! Você dominou todo o conteúdo!")
    elif pontos >= total / 2:
        st.info("Muito bem! Continue praticando para gabaritar.")
    else:
        st.warning("Bom esforço! Revise as explicações para melhorar na próxima.")

    if st.button("Jogar Novamente", type="primary"):
        reiniciar_jogo()
        st.rerun()

# Tela 3: Pergunta Ativa
else:
    q_idx = st.session_state.pergunta_atual_idx
    pergunta_data = st.session_state.perguntas_sorteadas[q_idx]

    st.caption(
        f"Matéria: {st.session_state.tema_escolhido} | Pergunta {q_idx + 1} de"
        f" {len(st.session_state.perguntas_sorteadas)}"
    )
    st.progress((q_idx) / len(st.session_state.perguntas_sorteadas))

    st.subheader(pergunta_data["pergunta"])

    # Opções com Radio Button (X)
    opcao_selecionada = st.radio(
        "Escolha a alternativa correta:",
        pergunta_data["opcoes"],
        disabled=st.session_state.respondido,
        key=f"q_{q_idx}",
    )

    if not st.session_state.respondido:
        if st.button("Confirmar Resposta", type="primary"):
            st.session_state.respondido = True
            if opcao_selecionada == pergunta_data["correta"]:
                st.session_state.pontos += 1
                st.session_state.resposta_correta_flag = True
            else:
                st.session_state.resposta_correta_flag = False
            st.rerun()
    else:
        # Exibe o feedback
        if st.session_state.resposta_correta_flag:
            st.success("✅ Resposta Correta!")
        else:
            st.error(f"❌ Resposta Incorreta!")
            st.info(f"👉 **A resposta certa é:** {pergunta_data['correta']}")

        # Explicação detalhada
        st.markdown(f"**📚 Explicação:** {pergunta_data['explicacao']}")

        # Botão para avançar
        if st.button("Próxima Pergunta ➡️", type="primary"):
            st.session_state.pergunta_atual_idx += 1
            st.session_state.respondido = False
            st.rerun()
