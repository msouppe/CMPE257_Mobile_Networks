# Get Java version 8_jdk Image
FROM anapsix/alpine-java:8_jdk_unlimited

# Install Python, Ant and packages for scripts
RUN apk --no-cache add python py-pip apache-ant && pip install --upgrade pip && pip install java-random pyyaml jinja2
