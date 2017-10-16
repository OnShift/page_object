FROM python:3

RUN apt-get update && \
  apt-get install -y build-essential && \
    apt-get install -y python-dev libffi-dev && \
    apt-get -yqq install curl unzip && \
    apt-get -yqq  install libnss3 xvfb && \
    apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

# Install Chrome Driver
RUN CHROMEDRIVER_VERSION=2.33 && \
    mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    rm /tmp/chromedriver_linux64.zip && \
    chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
    ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver

#Install Chrome
RUN wget -nv -O - http://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update -qqy \
    && apt-get -qqy install \
    google-chrome-stable \
    && rm -rf /var/lib/apt/lists/* \
    && rm /etc/apt/sources.list.d/google-chrome.list

WORKDIR app

COPY src src
COPY features features
COPY specs specs
COPY setup.py setup.py
COPY requirements.pip requirements.pip
COPY Makefile Makefile

RUN pip install -r requirements.pip

ENV BROWSER=HEADLESS

CMD ["make", "test"]
