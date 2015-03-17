# zodb
#
# VERSION 0.0.1
# vi: set ft=Dockerfile :
# vi: set nu :

FROM uralbash/docker-ubuntu:latest
MAINTAINER Dmitry Svintsov <root@uralbash.ru>

USER vagrant

## Python
ADD install_py.sh /tmp/install_py.sh
ADD install_zodb.sh /tmp/install_zodb.sh
RUN /tmp/install_py.sh
RUN /tmp/install_zodb.sh

USER root
