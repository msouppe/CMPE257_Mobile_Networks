FROM openjdk:9.0.4-12-jdk-slim-sid

RUN apt update && \
    apt install -y --no-install-recommends \
      python-minimal ant git build-essential \
      binutils-msp430 gcc-msp430 msp430-libc msp430mcu \
      mspdebug gcc-arm-none-eabi gdb-arm-none-eabi \
      libncurses5-dev libfontconfig1 && \
    apt install -y python-pip && \
    apt autoremove && \
    apt autoclean && \
    pip install java-random pyyaml jinja2 && \
    rm -rf /.cache/pip

ADD contiki.tgz /root/
