# start from base
FROM ubuntu:latest
MAINTAINER Prakhar Srivastav <prakhar@prakhar.me>

# install system-wide deps for python and node
RUN apt-get -yqq update
RUN apt-get -yqq install python-pip python-dev curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash
RUN apt-get install -yq nodejs

# copy our application code
ADD serv /opt/serv
WORKDIR /opt/serv

# fetch app specific deps
RUN npm install
RUN npm run build
RUN pip install -r requirements.txt 
RUN install json 

# expose port
EXPOSE 5000

# start app
CMD [ "python", "./main.py" ]
