FROM python:alpine3.16
WORKDIR /app
ENV BOT_NAME='Weather API TP1'
RUN pip3 install --no-cache-dir -Iv requests===2.27.1
COPY . .
CMD [ "python3", "weather.py"]

