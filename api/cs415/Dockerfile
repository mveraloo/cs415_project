FROM ubuntu
RUN apt update -y
RUN apt-get install python3-pip -y
RUN apt-get install python3-dev -y
RUN apt-get install default-libmysqlclient-dev -y
RUN apt-get install build-essential -y
RUN apt install apache2 -y
RUN apt install libapache2-mod-wsgi-py3 -y
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

COPY . /cs415/
WORKDIR /cs415
RUN pip install -r requirements.txt

COPY 000-default.conf /etc/apache2/sites-available/

EXPOSE 80