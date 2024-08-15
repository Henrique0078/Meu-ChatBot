# Jarvis - Inteligência Artificial

## Tutorial: Como Iniciar a API Jarvis

Este tutorial fornece instruções para iniciar a API Jarvis, que responde a perguntas usando um modelo de inteligência artificial.

## Passo 1: Clone o Repositório

Primeiro, você precisa clonar o repositório que contém o código da API. Execute o seguinte comando no terminal:

```bash
git clone https://github.com/Henrique0078/Meu-ChatBot.git
```

## Passo 2: Navegue para o Diretório do Projeto

Após clonar o repositório, navegue para o diretório do projeto:

```bash
cd jarvis-api
```
Substitua jarvis-api pelo nome do diretório onde o repositório foi clonado.

## Passo 3: Instale as Dependências

O projeto utiliza algumas bibliotecas Python que precisam ser instaladas. Essas bibliotecas estão listadas no arquivo `requirements.txt`. Instale as dependências executando:

```bash
pip install -r requirements.txt
```
Isso instalará todas as bibliotecas necessárias para executar o projeto, incluindo Flask, Flask-CORS, Transformers e pandas.

## Passo 4: Inicie a API

Com as dependências instaladas, você pode iniciar o servidor Flask que executa a API. Para isso, execute:

```bash
python app.py
```
E pronto, agora, a API esta funcionando.
## Descrição do Projeto

**Jarvis** é uma inteligência artificial desenvolvida para fornecer respostas a perguntas de forma eficiente. Utilizando modelos de processamento de linguagem natural, o Jarvis pode responder a perguntas com base em um contexto pré-carregado e um conjunto de perguntas e respostas predefinidas. 

Este projeto é construído com **Flask** e usa o modelo **DistilBERT** da biblioteca **Transformers** para realizar a tarefa de perguntas e respostas.

## Funcionalidades

- **Resposta a Perguntas:** Jarvis pode responder a perguntas com base em um contexto fornecido e em um dicionário de perguntas e respostas predefinidas.
- **Fallback para Modelos de QA:** Se uma pergunta não corresponder a nenhuma entrada predefinida, o Jarvis utiliza um modelo de QA para encontrar a melhor resposta possível com base no contexto.

## Arquitetura

1. **Pipeline de QA:** Utiliza o modelo `distilbert-base-uncased-distilled-squad` da biblioteca Transformers para responder perguntas baseadas em um contexto fornecido.
2. **Dicionário de Perguntas e Respostas:** Armazena respostas predefinidas para perguntas conhecidas, permitindo uma resposta rápida e precisa para questões frequentes.
3. **Contexto:** Texto carregado de um arquivo para fornecer informações adicionais ao modelo de QA.

## Endpoints da API

### Endpoint: `/ask`

#### Método: `POST`

#### Descrição

Este endpoint recebe uma pergunta em formato JSON e retorna uma resposta com base no dicionário de perguntas e respostas ou no modelo de QA.

#### Requisição

- **URL:** `/ask`
- **Método:** `POST`
- **Cabeçalhos:**
  - `Content-Type: application/json`
- **Corpo da Requisição:**

```json
{
  "question": "Sua pergunta aqui"
}
```
#### Resposta

- **Código de Status:**
  - `200 OK` - Se a pergunta for processada com sucesso.
  - `400 Bad Request` - Se a pergunta não for fornecida.

- **Corpo da Resposta:**

```json
{
  "question": "Sua pergunta aqui",
  "answer": "Resposta fornecida pela IA"
}
```
- **Exemplo de Resposta:**

```json
{
  "question": "Qual sua linguagem de programação preferida?",
  "answer": "Python é minha linguagem de programação preferida."
}
```
#### Erros

- **400 Bad Request:** Retornado quando o corpo da requisição está ausente ou malformado, ou quando a pergunta não é fornecida.

- **Exemplo de Erro:**

```json
{
  "error": "No question provided"
}
```
