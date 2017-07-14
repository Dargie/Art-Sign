FROM python:3.4

COPY requirement.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN wget https://deb.nodesource.com/setup_8.x -O /tmp/inode.sh && \
	chmod +x /tmp/inode.sh && \
	/tmp/inode.sh && \
	apt-get install nodejs -y

RUN npm install -g gulp

COPY start.sh /
RUN chmod 777 /start.sh

WORKDIR /code
VOLUME /code
EXPOSE 8000

RUN rm -rf /tmp/*
RUN touch /firstrun.tag

ENTRYPOINT /start.sh