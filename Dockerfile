# Use uma imagem base oficial do Python
FROM python:3.10-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do Python e substitua o Keras por tf-keras
RUN pip install --no-cache-dir -r requirements.txt
RUN pip uninstall -y keras
RUN pip install tf-keras

# Copie o restante do código da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta que o Flask usa (5000)
EXPOSE 5000

# Comando para rodar a aplicação Flask
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
