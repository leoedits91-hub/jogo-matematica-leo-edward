import base64
import os
import random
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Cantinho dos Estudos - 3º Ano",
    page_icon="✏️",
    layout="centered",
)

# Lista com os novos nomes simplificados
MEMES_VITORIA = [
    "memes/meme1.jpg",
    "memes/meme2.jpg",
    "memes/meme3.jpg",
    "memes/meme4.jpg",
]


def exibir_imagem_garantida(caminho_imagem):
    """Lê a imagem local e força a exibição via HTML/Base64 para evitar falhas do servidor."""
    if os.path.exists(caminho_imagem):
        with open(caminho_imagem, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        extensao = caminho_imagem.split(".")[-1].lower()
        mime_type = "image/png" if extensao == "png" else "image/jpeg"

        html_code = f"""
        <div style="display: flex; justify-content: center; align-items: center; margin-top: 15px; margin-bottom: 15px;">
            <img src="data:{mime_type};base64,{encoded_string}" style="max-width: 100%; height: auto; border-radius: 12px; box-shadow: 0px 4px 12px rgba(0,0,0,0.3);" />
        </div>
        """
        st.markdown(html_code, unsafe_allow_html=True)
    else:
        st.error(
            f"❌ O arquivo `{caminho_imagem}` não foi encontrado dentro da"
            " pasta `memes/` no GitHub. Verifique os nomes dos arquivos!"
        )


# Estilização visual
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f172a;
        background-image: 
            radial-gradient(#334155 1.5px, transparent 1.5px), 
            url("data:image/svg+xml,%3Csvg width='80' height='80' viewBox='0 0 80 80' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%231e293b' fill-opacity='0.4'%3E%3Cpath d='M0 0h40v40H0V0zm40 40h40v40H40V40z'/%3E%3Ccircle cx='20' cy='20' r='6' stroke='%23334155' stroke-width='1.5' fill='none'/%3E%3Cpath d='M60 15 l10 10 M70 15 l-10 10' stroke='%23334155' stroke-width='1.5'/%3E%3C/g%3E%3C/svg%3E");
        background-size: 30px 30px, 120px 120px;
        color: #F8FAFC;
    }
    
    div.block-container {
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(8px);
        padding: 2rem;
        border-radius: 16px;
        border: 1px solid #1e293b;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
    }

    h1, h2, h3, h4, label, .stMarkdown {
        color: #FFFFFF !important;
    }

    div[data-testid="stRadio"] > label {
        color: #F8FAFC !important;
        font-size: 1.1rem !important;
    }

    div.stButton > button:first-child {
        background-color: #2563EB !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.6rem 1.2rem !important;
        font-weight: bold !important;
        font-size: 1rem !important;
        transition: all 0.2s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #1D4ED8 !important;
        transform: translateY(-2px);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Banco de perguntas
BANCO_PERGUNTAS = {
    "🏃‍♂️ Educação Física - Danças e Ritmos": [
        {
            "pergunta": (
                "Qual destas danças é de roda, super tradicional no Brasil e"
                " reúne todo mundo de mãos dadas?"
            ),
            "opcoes": ["Ciranda", "Hip-hop", "Ballet clássico", "Tango"],
            "correta": "Ciranda",
            "explicacao": (
                "A Ciranda é uma dança comunitária onde os participantes dão as"
                " mãos em roda. Ela representa união e é super forte na cultura"
                " de Pernambuco."
            ),
        },
        {
            "pergunta": (
                "Quando marcamos o ritmo, a velocidade rápida ou lenta e as"
                " pausas dos passos, estamos usando qual elemento da dança?"
            ),
            "opcoes": ["Tempo", "Espaço", "Peso do corpo", "Figurino"],
            "correta": "Tempo",
            "explicacao": (
                "O elemento 'Tempo' controla o ritmo do movimento, as aceleradas"
                " e aquelas paradinhas estratégicas durante a música."
            ),
        },
        {
            "pergunta": (
                "Famoso pelos passos rápidos e pelos guarda-chuvas coloridos,"
                " o Frevo surgiu em qual estado?"
            ),
            "opcoes": [
                "Pernambuco",
                "Rio de Janeiro",
                "Rio Grande do Sul",
                "Bahia",
            ],
            "correta": "Pernambuco",
            "explicacao": (
                "O Frevo nasceu nas ruas de Pernambuco! Ele mistura acrobacias,"
                " capoeira e o som contagiante dos metais."
            ),
        },
        {
            "pergunta": (
                "O que melhor define as Danças Urbanas (como o Hip-hop e Street"
                " Dance)?"
            ),
            "opcoes": [
                (
                    "Movimentos fortes, ritmo marcante e criação nas ruas e"
                    " bairros"
                ),
                "Dança de salão em pares usando roupas da época do império",
                "Passos lentos apresentados apenas com sapatilhas de ponta",
                "Apresentações silenciosas e sem nenhum acompanhamento de som",
            ],
            "correta": (
                "Movimentos fortes, ritmo marcante e criação nas ruas e"
                " bairros"
            ),
            "explicacao": (
                "Elas nasceram nos grandes centros urbanos como forma de"
                " expressão dos jovens, misturando criatividade e muita"
                " atitude."
            ),
        },
        {
            "pergunta": (
                "Mudar de direção (ir pra frente, pra trás, fazer curvas ou"
                " abaixar) explora qual área da dança?"
            ),
            "opcoes": ["Espaço", "Alimentação", "Apenas a música", "Figurino"],
            "correta": "Espaço",
            "explicacao": (
                "O Espaço é o lugar onde o corpo se desloca. Ele envolve"
                " trajetórias, alturas (alto, médio, baixo) e direções."
            ),
        },
        {
            "pergunta": (
                "Em qual época do ano a gente mais dança a Quadrilha no"
                " Brasil?"
            ),
            "opcoes": [
                "Festas Juninas",
                "Carnaval de Rua",
                "Ano Novo",
                "Férias de Verão",
            ],
            "correta": "Festas Juninas",
            "explicacao": (
                "A Quadrilha é a marca registrada de junho e julho! Ela recria"
                " comemorações caipiras com muita música e passos animados em"
                " pares."
            ),
        },
        {
            "pergunta": (
                "O Samba de Roda é um patrimônio cultural do Brasil. Em qual"
                " região ele é mais tradicional?"
            ),
            "opcoes": [
                "Recôncavo Baiano (Bahia)",
                "Pampa Gaúcho",
                "Pantanal",
                "Serra Gaúcha",
            ],
            "correta": "Recôncavo Baiano (Bahia)",
            "explicacao": (
                "Ele nasceu na Bahia, fruto da cultura afro-brasileira, unindo"
                " batucada, palmas e muita dança no meio da roda."
            ),
        },
    ],
    "🌍 Geografia - Campo, Cidade e Paisagens": [
        {
            "pergunta": (
                "Qual é a diferença principal entre morar na cidade (área"
                " urbana) e no campo (área rural)?"
            ),
            "opcoes": [
                (
                    "A cidade tem mais prédios, lojas e serviços; o campo é"
                    " focado na agricultura e natureza"
                ),
                "O campo tem mais avenidas movimentadas e viadutos",
                "A cidade é onde ficam todas as plantações de grãos do país",
                "Não há diferença nenhuma, os dois ambientes são iguais",
            ],
            "correta": (
                "A cidade tem mais prédios, lojas e serviços; o campo é"
                " focado na agricultura e natureza"
            ),
            "explicacao": (
                "A área urbana concentra casas, lojas e fábricas juntas. Já a"
                " área rural tem grandes espaços verdes, sítios e fazendas."
            ),
        },
        {
            "pergunta": (
                "De que forma o campo e a cidade trabalham juntos no dia a dia?"
            ),
            "opcoes": [
                (
                    "O campo produz os alimentos e a cidade fabrica as"
                    " máquinas e roupas"
                ),
                "O campo só envia lixo e a cidade devolve plantas",
                "A cidade produz todas as frutas dentro dos apartamentos",
                "O campo não depende de nada que venha da cidade",
            ],
            "correta": (
                "O campo produz os alimentos e a cidade fabrica as"
                " máquinas e roupas"
            ),
            "explicacao": (
                "É uma troca constante! O campo manda comida e matéria-prima,"
                " enquanto a cidade fornece ferramentas, remédios e"
                " tecnologias."
            ),
        },
        {
            "pergunta": (
                "Qual destas opções mostra uma transformação da paisagem feita"
                " pelas pessoas?"
            ),
            "opcoes": [
                "Construção de uma ponte ou estrada",
                "Nascimento natural de um rio",
                "Um vulcão em erupção",
                "Chuva caindo na floresta",
            ],
            "correta": "Construção de uma ponte ou estrada",
            "explicacao": (
                "Quando o ser humano altera o espaço construindo casas, pontes ou"
                " ruas, chamamos de paisagem modificada ou cultural."
            ),
        },
        {
            "pergunta": (
                "O que significa a palavra 'Matéria-prima' nos nossos"
                " estudos?"
            ),
            "opcoes": [
                (
                    "O recurso vindo da natureza usado para fabricar um"
                    " produto"
                ),
                "O salgadinho embalado que compramos no mercado",
                "A caixa de papelão usada na mudança",
                "O valor em dinheiro cobrado na loja",
            ],
            "correta": (
                "O recurso vindo da natureza usado para fabricar um"
                " produto"
            ),
            "explicacao": (
                "É o elemento bruto natural (como o leite, o algodão ou o"
                " tomate) que depois é transformado na fábrica em queijo, roupa"
                " ou molho."
            ),
        },
        {
            "pergunta": (
                "Como se chama a atividade do campo responsável por criar bois,"
                " vacas, galinhas e porcos?"
            ),
            "opcoes": [
                "Pecuária",
                "Agricultura",
                "Pesca de mar",
                "Comércio de rua",
            ],
            "correta": "Pecuária",
            "explicacao": (
                "A Pecuária cuida da criação dos animais para a produção de"
                " alimentos como leite, ovos, carnes e também de materiais como"
                " o couro."
            ),
        },
        {
            "pergunta": (
                "Coletar açaí, castanhas ou madeira direto da floresta sem ter"
                " plantado faz parte de qual atividade?"
            ),
            "opcoes": [
                "Extrativismo Vegetal",
                "Agricultura de Trator",
                "Pecuária Intensiva",
                "Construção Civil",
            ],
            "correta": "Extrativismo Vegetal",
            "explicacao": (
                "O extrativismo vegetal acontece quando retiramos produtos que a"
                " própria natureza já produziu sozinha na floresta."
            ),
        },
        {
            "pergunta": (
                "O que acontece quando o lixo das cidades é jogado na rua de"
                " forma errada?"
            ),
            "opcoes": [
                "Entope bueiros e gera enchentes nas ruas",
                "Limpa os rios de forma automática",
                "Ajuda as árvores a crescerem mais rápido",
                "Faz o trânsito fluir com mais facilidade",
            ],
            "correta": "Entope bueiros e gera enchentes nas ruas",
            "explicacao": (
                "A água da chuva não consegue escorrer pelos bueiros entupidos"
                " de lixo, provocando alagamentos e sujeira pela cidade."
            ),
        },
    ],
}

TOTAL_PERGUNTAS = 5

# Controle de estado
if "pontos" not in st.session_state:
    st.session_state.pontos = 0
if "pergunta_atual" not in st.session_state:
    st.session_state.pergunta_atual = 0
if "lista_perguntas" not in st.session_state:
    st.session_state.lista_perguntas = []
if "tema" not in st.session_state:
    st.session_state.tema = None
if "respondido" not in st.session_state:
    st.session_state.respondido = False
if "acertou" not in st.session_state:
    st.session_state.acertou = False


def resetar():
    st.session_state.pontos = 0
    st.session_state.pergunta_atual = 0
    st.session_state.lista_perguntas = []
    st.session_state.tema = None
    st.session_state.respondido = False
    st.session_state.acertou = False


# Cabeçalho do Quiz
st.title("📝 Cantinho dos Estudos")
st.write("Escolha a matéria, teste seus conhecimentos e aprenda praticando!")

st.divider()

# Tela 1: Escolha do Assunto
if st.session_state.tema is None:
    st.subheader("Selecione uma matéria:")
    opcao = st.radio("", list(BANCO_PERGUNTAS.keys()))

    st.write("")
    if st.button("Começar Exercícios 🚀", type="primary"):
        st.session_state.tema = opcao

        perguntas = [dict(p) for p in BANCO_PERGUNTAS[opcao]]
        random.shuffle(perguntas)

        for p in perguntas:
            random.shuffle(p["opcoes"])

        st.session_state.lista_perguntas = perguntas[:TOTAL_PERGUNTAS]
        st.rerun()

# Tela 2: Finalização
elif st.session_state.pergunta_atual >= len(st.session_state.lista_perguntas):
    st.balloons()
    st.subheader("🎉 Quiz Concluído!")

    total = len(st.session_state.lista_perguntas)
    pontos = st.session_state.pontos

    st.info(f"Sua pontuação final: **{pontos} de {total} acertos**")

    # REGRA: Acertou 5 de 5 -> Exibe imagem obrigatoriamente
    if pontos == total:
        st.success("Excelente! Você gabaritou tudo!")

        meme_sorteado = random.choice(MEMES_VITORIA)
        exibir_imagem_garantida(meme_sorteado)

    elif pontos >= total / 2:
        st.success("Muito bem! Bom resultado!")
    else:
        st.warning("Bom esforço! Vale a pena tentar de novo para treinar.")

    st.write("")
    if st.button("Jogar Novamente 🔄", type="primary"):
        resetar()
        st.rerun()

# Tela 3: Questão em Exibição
else:
    idx = st.session_state.pergunta_atual
    dados = st.session_state.lista_perguntas[idx]

    progresso = idx / len(st.session_state.lista_perguntas)
    st.progress(progresso)

    st.caption(
        f"Matéria: **{st.session_state.tema}** | Questão {idx + 1} de"
        f" {len(st.session_state.lista_perguntas)}"
    )

    st.markdown(f"### {dados['pergunta']}")

    escolha = st.radio(
        "Marque a alternativa correta:",
        dados["opcoes"],
        disabled=st.session_state.respondido,
        key=f"p_{idx}",
    )

    st.write("")

    if not st.session_state.respondido:
        if st.button("Conferir Resposta", type="primary"):
            st.session_state.respondido = True
            if escolha == dados["correta"]:
                st.session_state.pontos += 1
                st.session_state.acertou = True
            else:
                st.session_state.acertou = False
            st.rerun()
    else:
        if st.session_state.acertou:
            st.success("✨ Acertou em cheio!")
        else:
            st.error("Ops, resposta errada!")
            st.info(f"💡 **A alternativa correta era:** {dados['correta']}")

        st.markdown(f"**Explicação:** {dados['explicacao']}")

        st.write("")
        if st.button("Próxima Questão ➔", type="primary"):
            st.session_state.pergunta_atual += 1
            st.session_state.respondido = False
            st.rerun()
