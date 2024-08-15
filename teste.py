from transformers import pipeline
import pandas as pd

# Carregar o pipeline para resposta a perguntas
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Carregar dados de perguntas e respostas
df = pd.read_csv('./qa_data.csv', delimiter=';', encoding='utf-8')

# Criar um dicionário de perguntas e respostas
qa_dict = pd.Series(df.Resposta.values, index=df.Pergunta).to_dict()

# Carregar o contexto do arquivo de texto
with open('./context.txt', 'r') as file:
    context = file.read()

# Função para responder perguntas usando o pipeline de QA
def ask_question(question):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# Função para responder perguntas com base em regras e fallback para o modelo de QA
def ask_question_with_fallback(question):
    # Normaliza a pergunta para lidar com variações
    normalized_question = question.strip().lower()
    for key in qa_dict.keys():
        if key.lower() in normalized_question:
            return qa_dict[key]
    # Se não estiver, utiliza o modelo de QA
    return ask_question(question)

# Testar a função
questions = [
    "Quem é o maior jogador de futebol?",
    "Qual é o melhor jogo do mundo?",
    "Quantos anos tem o Brasil?",
    "Em que linguagens de programação você programa?",
    "Qual sua linguagem de programação preferida?",
    "Quantos anos você tem?",
    "Qual o seu NOME?",
    "Quanto você pesa?",
    "demora quanto tempo pra ir para marte?",
    "quem é sua mãe?",
    "qual sua comida favorita?",
    "qual sua cor favorita?"
]

for question in questions:
    response = ask_question_with_fallback(question)
    print(f"Pergunta: {question}\nResposta: {response}\n")
