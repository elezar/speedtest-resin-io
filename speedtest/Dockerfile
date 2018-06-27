FROM resin/raspberrypi3-python:3.5-slim
MAINTAINER evanlezar@gmail.com

RUN pip install --no-cache-dir --upgrade \
        pip \
        speedtest-cli \
        fluent-logger

CMD ["speedtest", "--json"]
