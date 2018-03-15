FROM selenium/standalone-chrome:3.6.0

USER root

RUN  apt-get update && \ 
     apt-get install -y python3.5 python3-pip

WORKDIR app

COPY src src
COPY features features
COPY specs specs
COPY setup.py setup.py
COPY requirements.pip requirements.pip
COPY Makefile Makefile

RUN pip3 install -r requirements.pip

ENV BROWSER=HEADLESS

CMD ["make", "test"]


