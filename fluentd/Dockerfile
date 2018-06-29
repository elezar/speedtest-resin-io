FROM elezar/fluentd:v0.14.14-armhf-onbuild
LABEL maintainer Evan Lezar <evanlezar@gmail.com>

USER root

RUN apk add --update --virtual .build-deps \
        sudo build-base ruby-dev \
 # cutomize following instruction as you wish
 && gem install \
        fluent-plugin-out-http \
        fluent-plugin-bufferize \
 && gem sources --clear-all \
 && apk del .build-deps \
 && rm -rf /var/cache/apk/* \
           /home/fluent/.gem/ruby/*/cache/*.gem
