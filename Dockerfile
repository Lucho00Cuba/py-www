FROM python:3.8

ARG DUMB_INIT
ARG BUILD_DATE

LABEL maintainer="lomv0209@gmail.com" \
      owner="JustMe" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/Lucho00Cuba/py-www.git"

# ------ https://github.com/Yelp/dumb-init ------
ENV DUMB_INIT_VERSION=${DUMB_INIT:-1.2.0}
ADD https://github.com/Yelp/dumb-init/releases/download/v${DUMB_INIT_VERSION}/dumb-init_${DUMB_INIT_VERSION}_amd64 /bin/dumb-init
# -----------------------------------------------

ADD ./src /app
WORKDIR /app

RUN chmod +x /bin/dumb-init && pip install -r requirements.txt

ENTRYPOINT ["/bin/dumb-init"]
CMD ["python", "__main__.py"]