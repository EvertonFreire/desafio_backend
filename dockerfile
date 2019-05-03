FROM centos:7

MAINTAINER Everton Freire Segur <evertonsegur7@gmail.com>

RUN yum install -y epel-release

RUN yum install -y python python-pip && yum clean all

ADD ./desafio_backend_everton /etc/got-api/

RUN ln -sf /dev/stdout /var/log/messages

RUN pip install pip --upgrade 

RUN pip install flask flask-mysql jsonify mysql-connector 

EXPOSE 5000

CMD python /etc/got-api/src/app/got_desafio.py
