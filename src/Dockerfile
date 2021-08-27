FROM python:3.9-slim-buster

WORKDIR /usr/src/app
COPY . .
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]
