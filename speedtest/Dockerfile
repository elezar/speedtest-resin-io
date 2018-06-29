FROM resin/armhf-alpine:3.7
LABEL maintainer evanlezar@gmail.com

RUN apk update \
 && apk upgrade \
 && apk add --no-cache \
        python3 \
 && rm -rf /var/cache/apk/* \
 && rm -rf /tmp/* /var/tmp/* \
 && pip3 install --no-cache-dir --upgrade \
        pip

RUN mkdir -p /opt/speedtest
WORKDIR /opt/speedtest

COPY requirements.txt /opt/speedtest/
RUN pip3 install --no-cache-dir -r requirements.txt && rm requirements.txt
COPY driver.py /opt/speedtest/

ENV TEST_INTERVAL_SECONDS=300
ENV FLUENT_HOSTNAME=localhost
ENV FLUENT_PORT=24224
ENV CONNECTION_ID auto

CMD python3 /opt/speedtest/driver.py --interval ${TEST_INTERVAL_SECONDS} --fluent-host ${FLUENT_HOSTNAME} --fluent-port ${FLUENT_PORT} --connection-id ${CONNECTION_ID}
