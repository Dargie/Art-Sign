FROM python:3.4

WORKDIR /code

COPY requirement.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY start.sh /

RUN chmod 777 /start.sh

VOLUME /code

EXPOSE 8000

RUN rm -rf /tmp/*

RUN touch /firstrun.tag

ENTRYPOINT /start.sh