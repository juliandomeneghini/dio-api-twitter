# Use uma imagem base Python
FROM python:3.8

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o código do projeto para o diretório de trabalho
COPY . .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta em que a aplicação irá rodar
EXPOSE 8080

# Comando para rodar a aplicação quando o container for iniciado
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
