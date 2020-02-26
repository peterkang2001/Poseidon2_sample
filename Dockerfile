FROM python:3.7.6-alpine3.10

MAINTAINER peterkang2001@gmail.com
USER root
ENV TIME_ZONE Asia/Shanghai

RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.9/main/" > /etc/apk/repositories \
    && apk add --no-cache -U tzdata \
    && ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime \
    && echo "${TIME_ZONE}" > /etc/timezone \


RUN mkdir /app\
    && mkdir /logs

ADD . /app
WORKDIR /app

CMD ["/bin/sh"]