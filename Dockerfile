FROM python:3

ENV USERNAME=username
ENV PASSWORD=password

WORKDIR /usr/src/keyserver

EXPOSE 5000

COPY . .
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.5.0/wait /wait
RUN chmod +x /wait

RUN mv config.py /usr/src/keyserver/keyserv/
RUN pip install -U -r requirements.txt

CMD /wait

ENTRYPOINT [ "bash" ]
CMD [ "entry.sh", "$USERNAME", "$PASSWORD" ]
