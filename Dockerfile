FROM debian:11
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install python3 python3-pip git curl ffmpeg mediainfo -y
ARG USER=root
USER $USER
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY start.sh start.sh
COPY app.py app.py
COPY .env .env
EXPOSE 5000
RUN chmod +x /app/start.sh
ENTRYPOINT ["./start.sh"]
