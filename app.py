from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import pandas as pd

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas e origens

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

@app.route('/')
def teste():
    return "Jarvis está no Ar."

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    
    answer = ask_question_with_fallback(question)
    return jsonify({'question': question, 'answer': answer})

if __name__ == '__main__':
    app.run(debug=False)
