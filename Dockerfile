from alpine:latest
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip \
    && apk add sqlite 

RUN echo "http://dl-8.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
  && apk update \
  && apk add py3-numpy py3-pandas

WORKDIR \App
COPY . \App

RUN pip install Click==7.0
RUN pip install Flask==1.1.1
RUN pip install Flask-SQLAlchemy==2.4.1
RUN pip install itsdangerous==1.1.0
RUN pip install Jinja2==2.10.3
RUN pip install MarkupSafe==1.1.1
RUN pip install python-dateutil==2.8.0
RUN pip install pytz==2019.3
RUN pip install six==1.12.0
RUN pip install SQLAlchemy==1.3.10
RUN pip install Werkzeug==0.16.0

RUN pwd
EXPOSE 5000
ENTRYPOINT  ["python3"]
CMD ["App/api_v1.py"]
   