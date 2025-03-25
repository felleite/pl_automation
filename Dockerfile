FROM python:3.11-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    curl unzip chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Define variáveis de ambiente para o Chrome
ENV CHROMEDRIVER_PATH /usr/bin/chromedriver
ENV GOOGLE_CHROME_BIN /usr/bin/chromium

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos para o container
COPY requirements.txt .
COPY main.py .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
