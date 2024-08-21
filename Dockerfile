# Use uma imagem base oficial do Python
FROM python:3.10-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do Python e substitua o Keras por tf-keras
RUN pip install --no-cache-dir -r requirements.txt && \
    pip uninstall -y keras && \
    pip install tf-keras

# Copie o restante do código da aplicação para o diretório de trabalho
COPY . .

# Defina a variável de ambiente PORT com um valor padrão
ENV PORT=5000

# Exponha a porta que a aplicação usará
EXPOSE 5000

# Comando para rodar a aplicação Flask, usando a variável de ambiente PORT
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:${PORT}", "app:app"]
