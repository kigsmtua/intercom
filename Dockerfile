FROM python:3.6-slim
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app/src
COPY . /usr/src/app
CMD python main.py
