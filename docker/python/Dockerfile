FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /mentiz
WORKDIR /mentiz
ADD . /mentiz/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install mysqlclient
COPY . /mentiz/

ENTRYPOINT ["./docker/python/entrypoint.sh"]