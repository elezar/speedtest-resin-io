FROM resin/armhf-alpine:3.7
LABEL maintainer evanlezar@gmail.com

RUN apk update \
 && apk upgrade \
 && apk add --no-cache \
        python3 \
 && pip3 install --no-cache-dir --upgrade \
        pip \
 && pip3 install --no-cache-dir --upgrade \
        fluent-logger \
        speedtest-cli \
 && rm -rf /var/cache/* \
 && rm -rf /root/.cache/*

RUN mkdir -p /opt/speedtest
WORKDIR /opt/speedtest
COPY driver.py /opt/speedtest/

ENV TEST_INTERVAL_SECONDS=300
ENV FLUENT_HOSTNAME=localhost
ENV FLUENT_PORT=24224
ENV CONNECTION_ID auto

CMD python3 /opt/speedtest/driver.py --interval ${TEST_INTERVAL_SECONDS} --fluent-host ${FLUENT_HOSTNAME} --fluent-port ${FLUENT_PORT} --connection-id ${CONNECTION_ID}
