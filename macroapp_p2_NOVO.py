import streamlit as st
import random
from datetime import datetime


# Função para exibir pergunta com melhor UI
def mostrar_pergunta(pergunta, resposta_correta, justificativa, index, total_perguntas):
    # Cartão com borda e sombra para cada pergunta
    with st.container():
        st.markdown(f"""
        <div style="padding: 20px; border-radius: 10px; background-color: #1E293B; 
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px;">
            <h4 style="color: #F9FAFB; margin-bottom: 15px;">Questão {index}/{total_perguntas}</h4>
            <p style="font-size: 16px; margin-bottom: 20px;">{pergunta}</p>
        </div>
        """, unsafe_allow_html=True)

        # Botões mais atrativos para as respostas
        col1, col2 = st.columns(2)
        with col1:
            verdadeiro = st.button("Verdadeiro (V)", key=f"V_{index}",
                                   use_container_width=True,
                                   type="secondary")  # Always use secondary type initially
        with col2:
            falso = st.button("Falso (F)", key=f"F_{index}",
                              use_container_width=True,
                              type="secondary")  # Always use secondary type initially

        # Verificar resposta quando o usuário clicar
        resposta_usuario = None
        if verdadeiro:
            resposta_usuario = "V"
        elif falso:
            resposta_usuario = "F"

        if resposta_usuario is not None:
            if resposta_usuario == resposta_correta:
                st.success("✅ CORRETO! Muito bem!")
            else:
                st.error(f"❌ INCORRETO! A resposta correta é: {resposta_correta}")

            # Justificativa com estilo melhorado
            st.markdown(f"""
            <div style="padding: 15px; border-left: 4px solid #F9FAFB; 
                        background-color: black; margin: 10px 0px 20px 0px;">
                <strong>Justificativa:</strong> {justificativa}
            </div>
            """, unsafe_allow_html=True)

    # Divisor visualmente mais atraente
    st.markdown("<hr style='margin: 30px 0; border: none; height: 1px; background-color: #E5E7EB;'>",
                unsafe_allow_html=True)


# Função para criar seção de tópico
def criar_secao(titulo, descricao, perguntas, emoji):
    # Cabeçalho de seção com melhor estilo e ícone
    st.markdown(f"""
    <div style="display: flex; align-items: center; margin: 30px 0 20px 0;">
        <div style="font-size: 30px; margin-right: 15px;">{emoji}</div>
        <h2 style="margin: 0; color: #F9FAFB;">{titulo}</h2>
    </div>
    <p style="margin-bottom: 25px; color: #4B5563;">{descricao}</p>
    """, unsafe_allow_html=True)

    # Contador de acertos para esta seção
    acertos = 0
    total = len(perguntas)

    # Exibir perguntas
    for i, q in enumerate(perguntas):
        mostrar_pergunta(q["pergunta"], q["resposta_correta"], q["justificativa"], i + 1, total)

    # Barra de progresso
    st.progress(1.0)
    st.markdown(f"<p style='text-align: right;'>Seção concluída!</p>", unsafe_allow_html=True)


def main():
    # Configuração da página com tema consistente
    st.set_page_config(
        page_title="Quiz de Macroeconomia",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # CSS personalizado para melhorar a aparência geral
    st.markdown("""
    <style>
    .stButton button {
        border-radius: 8px;
        padding: 10px 15px;
        font-weight: 500;
        transition: all 0.3s;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1000px;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .css-1aumxhk {
        background-color: #F9FAFB;
    }
    </style>
    """, unsafe_allow_html=True)

    # Barra lateral com instruções e estatísticas
    with st.sidebar:
        st.title("🧠 Quiz para P2 de Macro III")
        st.subheader("por Bernardo Louzada")

        st.markdown("---")

        st.subheader("📝 Instruções")
        st.markdown("""
        Bem-vindo ao Quiz de Macroeconomia!

        - Responda às questões marcando **Verdadeiro (V)** ou **Falso (F)**
        - Veja imediatamente se acertou e leia a justificativa
        - As perguntas estão organizadas por tópicos
        - Use o menu abaixo para navegar entre as seções
        """)

        st.markdown("---")

        # Menu de navegação
        st.subheader("🧭 Navegação")
        menu = st.radio(
            "Selecione um tópico:",
            ["Página Inicial",
             "Teoria das Expectativas Racionais",
             "Ciclos Reais de Negócios",
             "Modelos Novo-Keynesianos",
             "Mercado de Trabalho e Assimetrias"]
        )

    # Carrega as perguntas (mantendo as mesmas do código original)
    perguntas_TER = [
        # Do primeiro PDF – questões sobre TER (Q3 e Q4)
        {
            "pergunta": "Na TER, um choque monetário não modifica de forma permanente a oferta real.",
            "resposta_correta": "F",
            "justificativa": "Os choques monetários têm efeitos temporários, pois os agentes ajustam rapidamente suas expectativas."
        },
        {
            "pergunta": "Na função de oferta de Lucas, se o preço atual excede o preço esperado, a oferta real supera a oferta prevista.",
            "resposta_correta": "V",
            "justificativa": "Conforme Lucas, pt > p̂ implica que Y > Ŷ."
        },
        {
            "pergunta": "Na TER, o governo ajusta sua política monetária de acordo com o grau de realização das expectativas.",
            "resposta_correta": "F",
            "justificativa": "Os agentes já incorporam todas as informações disponíveis, tornando ineficaz a modificação da política com base em expectativas."
        },
        {
            "pergunta": "Na TER, o ciclo econômico não pode ser cumulativo.",
            "resposta_correta": "V",
            "justificativa": "Ciclos ocorrem a partir de choques exógenos e os ajustes das expectativas evitam processos cumulativos."
        },
        {
            "pergunta": "As curvas de Phillips na TER não se restringem apenas ao curto prazo.",
            "resposta_correta": "F",
            "justificativa": "A curva de Phillips é considerada vertical tanto no curto quanto no longo prazo na TER."
        },
        {
            "pergunta": "O ciclo econômico na TER não se explica exclusivamente por choques monetários.",
            "resposta_correta": "F",
            "justificativa": "Choques reais, como tecnológicos, também são determinantes para o ciclo econômico."
        },
        {
            "pergunta": "A Teoria das Expectativas Racionais não considera a existência de custos de ajuste na economia, o que limita sua capacidade de explicar certas flutuações econômicas.",
            "resposta_correta": "V",
            "justificativa": "A TER assume ajustes instantâneos, desconsiderando custos de mudança de preços e rigidez salarial."
        },
        # Do segundo PDF – conjunto 1
        {
            "pergunta": "Agentes formam suas expectativas utilizando todas as informações disponíveis, inclusive o modelo econômico vigente.",
            "resposta_correta": "V",
            "justificativa": "A TER parte do pressuposto de que os agentes são racionais e utilizam todo o conhecimento disponível."
        },
        {
            "pergunta": "Políticas monetárias e fiscais são sempre eficazes no curto prazo, pois os agentes não antecipam seus efeitos.",
            "resposta_correta": "F",
            "justificativa": "Os agentes antecipam os efeitos, o que torna essas políticas ineficazes tanto no curto quanto no longo prazo."
        },
        {
            "pergunta": "A curva de Phillips, segundo a TER, é vertical no curto e longo prazo.",
            "resposta_correta": "V",
            "justificativa": "Isso demonstra a ausência de trade-off entre inflação e desemprego na abordagem de expectativas racionais."
        },
        # Do segundo PDF – conjunto 2 (Crítica ao Keynesianismo)
        {
            "pergunta": "Políticas econômicas sistemáticas são ineficazes, pois os agentes ajustam antecipadamente suas expectativas.",
            "resposta_correta": "V",
            "justificativa": "A antecipação dos agentes neutraliza os efeitos de políticas sistemáticas."
        },
        {
            "pergunta": "A crítica da TER ao keynesianismo defende que choques de demanda agregada explicam flutuações persistentes.",
            "resposta_correta": "F",
            "justificativa": "A TER enfatiza que choques reais, e não apenas de demanda, explicam as flutuações econômicas."
        },
        {
            "pergunta": "A TER defende que modelos macroeconômicos devem incorporar microfundamentos, como o comportamento otimizador dos agentes.",
            "resposta_correta": "V",
            "justificativa": "Integrar microfundamentos é crucial para uma análise mais consistente do comportamento dos agentes."
        },
        # Do segundo PDF – conjunto 3 (Hipóteses do Modelo de Expectativas Racionais)
        {
            "pergunta": "Os agentes utilizam toda a informação disponível para formar expectativas, sem acesso a informações futuras.",
            "resposta_correta": "V",
            "justificativa": "Essa é uma hipótese central da TER."
        },
        {
            "pergunta": "O modelo assume que os erros de previsão são sempre nulos, já que os agentes possuem informações perfeitas.",
            "resposta_correta": "F",
            "justificativa": "Erros de previsão ocorrem e são considerados ruído branco no modelo."
        },
        {
            "pergunta": "Políticas econômicas não sistemáticas podem ter efeitos temporários sobre o produto e o emprego.",
            "resposta_correta": "V",
            "justificativa": "Políticas inesperadas podem surpreender os agentes e gerar efeitos transitórios antes do ajuste completo das expectativas."
        }
    ]

    perguntas_ciclos = [
        {
            "pergunta": "Os ciclos econômicos na Teoria dos Ciclos Reais são causados principalmente por choques monetários.",
            "resposta_correta": "F",
            "justificativa": "Os modelos apontam choques reais, como inovações tecnológicas, como principais motores dos ciclos."
        },
        {
            "pergunta": "Um choque de produtividade positivo temporário leva a um aumento do salário e, devido ao efeito substituição, a um acréscimo na oferta de trabalho.",
            "resposta_correta": "F",
            "justificativa": "Choques positivos tendem a aumentar o salário e a oferta de trabalho, não a reduzi-la."
        },
        {
            "pergunta": "Na Teoria dos Ciclos Reais, o ciclo econômico reflete a manutenção das condições de maximização dos agentes.",
            "resposta_correta": "V",
            "justificativa": "Os agentes respondem a choques exógenos de forma a manter suas condições de maximização."
        },
        {
            "pergunta": "Nos modelos RBC, os ciclos são causados exclusivamente por choques de demanda agregada.",
            "resposta_correta": "F",
            "justificativa": "Os modelos RBC enfatizam choques reais, não apenas de demanda, como fonte dos ciclos."
        },
        {
            "pergunta": "Um aumento na produtividade gera, de forma temporária, elevação no emprego e no produto nos modelos RBC.",
            "resposta_correta": "V",
            "justificativa": "Choques de produtividade têm efeitos positivos transitórios sobre a economia."
        },
        {
            "pergunta": "A flexibilidade de salários e preços nos modelos RBC garante o ajuste rápido dos mercados.",
            "resposta_correta": "V",
            "justificativa": "Essa flexibilidade elimina desequilíbrios, promovendo ajustes eficientes."
        },
        {
            "pergunta": "Nos Modelos de Ciclos Reais, um choque negativo de produtividade reduz temporariamente o emprego, mas não afeta o produto de longo prazo.",
            "resposta_correta": "F",
            "justificativa": "A redução da produtividade pode afetar o crescimento do capital e do trabalho, impactando o produto no longo prazo."
        }
    ]

    perguntas_nk = [
        {
            "pergunta": "No caso da análise microeconômica de Mankiw (duopólio), o ótimo é alcançado mesmo com preços parcialmente rígidos.",
            "resposta_correta": "F",
            "justificativa": "A rigidez de preços gera falhas de coordenação e conduz a resultados subótimos."
        },
        {
            "pergunta": "As falhas de coordenação no mercado decorrem de externalidades de demanda entre as empresas.",
            "resposta_correta": "V",
            "justificativa": "Decisões interdependentes podem gerar externalidades que afetam a eficiência do mercado."
        },
        {
            "pergunta": "Os efeitos da recessão são integralmente compensados somente quando os preços são totalmente flexíveis.",
            "resposta_correta": "F",
            "justificativa": "Mesmo com flexibilidade, podem persistir efeitos devido a ineficiências e atrasos de ajuste."
        },
        {
            "pergunta": "No modelo de Mankiw, a rigidez dos preços é explicada pelos custos de cardápio (menu costs).",
            "resposta_correta": "V",
            "justificativa": "Os custos associados à mudança de preços explicam a rigidez observada."
        },
        {
            "pergunta": "A histerese no mercado de trabalho implica que choques temporários podem ter efeitos permanentes sobre o emprego.",
            "resposta_correta": "V",
            "justificativa": "Choques podem alterar a dinâmica do mercado de trabalho de forma duradoura."
        },
        {
            "pergunta": "Akerlof, Grossman e Stiglitz defendem que a qualidade dos bens pode variar independentemente do preço, refutando o postulado de homogeneidade.",
            "resposta_correta": "V",
            "justificativa": "Em mercados com assimetrias de informação, o preço não reflete necessariamente a qualidade."
        },
        {
            "pergunta": "No modelo de Mankiw, os custos de menu tornam ajustes frequentes de preços inviáveis, mesmo com pequenas mudanças na demanda.",
            "resposta_correta": "F",
            "justificativa": "Custos de menu tornam o ajuste oneroso, levando as empresas a alterarem preços com menos frequência."
        },
        {
            "pergunta": "A rigidez de preços pode provocar falhas de coordenação e resultar em equilíbrios subótimos.",
            "resposta_correta": "V",
            "justificativa": "A dificuldade de ajustes simultâneos pode gerar distorções na economia."
        },
        {
            "pergunta": "A rigidez nominal de preços é irrelevante para a política monetária, pois não afeta o produto real.",
            "resposta_correta": "F",
            "justificativa": "A rigidez nominal pode amplificar os efeitos das políticas monetárias, afetando o produto no curto prazo."
        }
    ]

    perguntas_mercado = [
        {
            "pergunta": "No mercado de trabalho, o conceito de salário de eficiência sugere que salários mais altos podem elevar a produtividade dos trabalhadores.",
            "resposta_correta": "V",
            "justificativa": "Salários elevados podem reduzir a rotatividade e incentivar maior empenho, aumentando a produtividade."
        },
        {
            "pergunta": "De acordo com a teoria neoclássica, um aumento na taxa de juros sempre resulta em maior oferta de crédito no mercado bancário.",
            "resposta_correta": "F",
            "justificativa": "A elevação dos juros pode aumentar o risco de inadimplência e, consequentemente, reduzir a oferta de crédito."
        },
        {
            "pergunta": "A assimetria de informação no mercado de trabalho pode ocasionar desemprego involuntário, mesmo quando os salários são flexíveis.",
            "resposta_correta": "V",
            "justificativa": "A dificuldade em distinguir entre trabalhadores produtivos e menos produtivos pode levar a ineficiências no emprego."
        },
        {
            "pergunta": "O fenômeno da histerese implica que recessões podem ter efeitos permanentes sobre o produto potencial da economia.",
            "resposta_correta": "V",
            "justificativa": "Recessões podem deixar cicatrizes, afetando a capacidade produtiva de forma duradoura."
        },
        {
            "pergunta": "O postulado de homogeneidade foi refutado por modelos que ressaltam a heterogeneidade e as assimetrias de informação entre os agentes.",
            "resposta_correta": "V",
            "justificativa": "Esses modelos mostram que qualidade e preço não estão necessariamente correlacionados em mercados reais."
        },
        {
            "pergunta": "A refutação do postulado de homogeneidade afirma que, em mercados com assimetria de informação, o preço sempre reflete a qualidade do bem.",
            "resposta_correta": "F",
            "justificativa": "Em mercados com informação imperfeita, preços podem não refletir qualidade, como destacado por Akerlof no problema do 'mercado de limões'"
        },
        {
            "pergunta": "Salários de eficiência não têm relevância para explicar o desemprego involuntário.",
            "resposta_correta": "F",
            "justificativa": "O conceito de salário de eficiência pode afetar a produtividade e, por consequência, os níveis de emprego."
        },
        {
            "pergunta": "Assimetrias de informação no mercado de trabalho podem levar à seleção adversa, prejudicando a alocação eficiente dos recursos humanos.",
            "resposta_correta": "V",
            "justificativa": "Quando os empregadores não conseguem diferenciar a qualidade dos candidatos, ocorre seleção adversa."
        },
        {
            "pergunta": "Problemas de moral hazard no mercado bancário são irrelevantes para a concessão de crédito.",
            "resposta_correta": "F",
            "justificativa": "O moral hazard aumenta o risco dos empréstimos, impactando negativamente a oferta de crédito."
        },
        {
            "pergunta": "Em mercados com informação perfeita, a regulação bancária seria desnecessária.",
            "resposta_correta": "V",
            "justificativa": "A informação perfeita permitiria ajustes eficientes nos contratos, reduzindo a necessidade de intervenção regulatória."
        }
    ]

    # Conteúdo principal baseado no menu selecionado
    if menu == "Página Inicial":
        # Página inicial com animação e introdução visual
        st.markdown("""
        <div style="text-align: center; padding: 40px 0;">
            <h1 style="font-size: 48px; color: #F9FAFB; margin-bottom: 20px;">Quiz de revisão para a P2 de Macro</h1>
            <p style="font-size: 20px; max-width: 800px; margin: 0 auto; color: #4B5563;">
                por: Bernardo Louzada.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Cards dos principais tópicos
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="padding: 20px; border-radius: 10px; background-color: #1E293B; 
                        box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; height: 250px;">
                <h3 style="color: #F9FAFB;">📝 Conteúdo do Quiz</h3>
                <ul style="margin-top: 15px;">
                    <li>Teoria das Expectativas Racionais</li>
                    <li>Ciclos Reais de Negócios</li>
                    <li>Modelos Novo-Keynesianos</li>
                    <li>Mercado de Trabalho e Assimetrias</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="padding: 20px; border-radius: 10px; background-color: #1E293B; 
                        box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; height: 250px;">
                <h3 style="color: #F9FAFB;">🎯 Como Usar</h3>
                <ol style="margin-top: 15px;">
                    <li>Escolha um tópico no menu lateral</li>
                    <li>Responda as questões clicando em V ou F</li>
                    <li>Veja a explicação após cada resposta</li>
                    <li>Retorne a qualquer momento para revisar</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style="padding: 20px; border-radius: 10px; background-color: #1E293B; 
                        box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; height: 520px;">
                <h3 style="color: #F9FAFB;">📊 Estatísticas do Quiz</h3>
                <div style="margin-top: 25px;">
                    <p style="font-size: 16px;">Total de questões: <strong>42</strong></p>
                    <p style="font-size: 16px;">Questões por tópico:</p>
                    <ul>
                        <li>Teoria das Expectativas Racionais: 16 questões</li>
                        <li>Ciclos Reais de Negócios: 7 questões</li>
                        <li>Modelos Novo-Keynesianos: 9 questões</li>
                        <li>Mercado de Trabalho: 10 questões</li>
                    </ul>
                    <p style="font-size: 16px; margin-top: 20px;">Tempo estimado: <strong>30-40 minutos</strong></p>
                </div>
            </div>
            """, unsafe_allow_html=True)

    elif menu == "Teoria das Expectativas Racionais":
        criar_secao(
            "Teoria das Expectativas Racionais (TER)",
            "Teste seus conhecimentos sobre como os agentes formam expectativas e como isso afeta a economia.",
            perguntas_TER,
            "📊"
        )

    elif menu == "Ciclos Reais de Negócios":
        criar_secao(
            "Modelos de Ciclos Reais de Negócios",
            "Avalie sua compreensão sobre como choques de produtividade podem afetar a economia.",
            perguntas_ciclos,
            "📈"
        )

    elif menu == "Modelos Novo-Keynesianos":
        criar_secao(
            "Modelos Novo-Keynesianos e Custos de Cardápio",
            "Teste seu conhecimento sobre rigidez de preços e seus efeitos na economia.",
            perguntas_nk,
            "🏛️"
        )

    elif menu == "Mercado de Trabalho e Assimetrias":
        criar_secao(
            "Mercado de Trabalho, Bancário e Assimetria de Informação",
            "Verifique sua compreensão sobre problemas de informação nos mercados reais.",
            perguntas_mercado,
            "💼"
        )


if __name__ == "__main__":
    main()
