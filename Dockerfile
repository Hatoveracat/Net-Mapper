FROM ubuntu:22.04
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install nmap -y
RUN apt-get install python3 -y
WORKDIR /src_code
COPY hostslist.py .
COPY ipandsubext.py .
COPY parsjson.py .


