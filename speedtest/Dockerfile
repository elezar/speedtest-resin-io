FROM resin/raspberrypi3-python:3.5-slim
LABEL maintainer evanlezar@gmail.com

RUN pip install --no-cache-dir --upgrade \
        pip

WORKDIR /opt/speedtest

COPY requirements.txt /opt/speedtest
RUN pip install -r requirements.txt && rm requirements.txt

COPY driver.py /opt/speedtest

ENV TEST_INTERVAL_SECONDS=300
ENV FLUENT_HOSTNAME=localhost
ENV FLUENT_PORT=24224

CMD ["/opt/speedtest/driver.py", "--interval", ${TEST_INTERVAL_SECONDS}, "--fluent-host", ${FLUENT_HOSTNAME}}, "--fluent-port", ${FLUENT_PORT}}]
