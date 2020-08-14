
FROM kalilinux/kali-rolling
RUN apt-get update && apt upgrade -y && apt-get install sudo

RUN apt-get install -y\
    coreutils \
    bash \
    nodejs \
    bzip2 \
    curl \
    figlet \
    gcc \
    g++ \
    git \
    aria2 \
    axel \
    libevent-dev \
    libjpeg-dev \
    libffi-dev \
    libpq-dev \
    libwebp-dev \
    libxml2 \
    libxml2-dev \
    libxslt-dev \
    musl \
    neofetch \
    libcurl4-openssl-dev \
    postgresql \
    postgresql-client \
    postgresql-server-dev-all \
    openssl \
    pv \
    jq \
    wget \
    python3 \
    python3-dev \
    python3-pip \
    libreadline-dev \
    sqlite \
    ffmpeg \
    libsqlite3-dev \
    chromium \
    zlib1g-dev \
    recoverjpeg \
    zip \
    megatools \
    libfreetype6-dev




RUN pip3 install --upgrade pip setuptools 
RUN git clone https://github.com/amitsharma123234/Plus /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/
RUN chmod +x /usr/local/bin/*
RUN python3 -m pip install --no-warn-script-location --no-cache-dir --upgrade -r requirements.txt
RUN sudo chmod o+r /usr/lib/python3/dist-packages/*
CMD ["python3","-m","userbot"]
