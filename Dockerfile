FROM mysql

ENV MYSQL_ROOT_PASSWORD=apiuserPass

COPY ./create /docker-entrypoint-initdb.d

EXPOSE 3306
