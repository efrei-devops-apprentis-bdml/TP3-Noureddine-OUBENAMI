FROM python:alpine3.16
WORKDIR /app
ENV BOT_NAME='Weather API TP1'
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8081
  CMD [ "python3", "api.py"]

