FROM openjdk:17.0.2-jdk-slim as java-base
COPY --from=python:3.11 /usr/local/bin/python /usr/local/bin/python

ENV SONAR_SCANNER_VERSION=5.0.0.2966
ENV SONAR_SCANNER_HOME=/opt/sonar-scanner

USER root
WORKDIR /opt

RUN apt-get update && \
    apt-get install -y wget unzip && \
    wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip && \
    unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip && \
    rm sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip && \
    mv sonar-scanner-${SONAR_SCANNER_VERSION}-linux ${SONAR_SCANNER_HOME} && \
    ln -s ${SONAR_SCANNER_HOME}/bin/sonar-scanner /usr/bin/sonar-scanner && \
    sed -i 's/use_embedded_jre=true/use_embedded_jre=false/g' ${SONAR_SCANNER_HOME}/bin/sonar-scanner

COPY sonar-project.properties ${SONAR_SCANNER_HOME}/conf/sonar-scanner.properties

#RUN sonar-scanner --version
