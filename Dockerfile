FROM python:alpine3.16
WORKDIR /app
ENV BOT_NAME='Weather API TP1'
RUN pip3 install --no-cache-dir -Iv requests===2.27.1
RUN pip3 install --no-cache-dir -Iv flask
COPY . .
EXPOSE 8081
  CMD [ "python3", "api.py"]

