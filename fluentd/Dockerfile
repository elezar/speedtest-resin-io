FROM elezar/fluentd:v0.14.14-armhf-onbuild
MAINTAINER Evan Lezar <evanlezar@gmail.com>

USER root

RUN apk add --update --virtual .build-deps \
        sudo build-base ruby-dev \
 # cutomize following instruction as you wish
 && sudo -u fluent gem install \
        fluent-plugin-out-http \
        fluent-plugin-bufferize \

 && sudo -u fluent gem sources --clear-all \
 && apk del .build-deps \
 && rm -rf /var/cache/apk/* \
           /home/fluent/.gem/ruby/2.3.0/cache/*.gem

USER fluent
