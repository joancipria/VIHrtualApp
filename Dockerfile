FROM ubuntu:18.04
ENTRYPOINT []
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip install --upgrade pip==20.2 && pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple 
ADD . /app/
RUN chmod +x /app/start_services.sh
CMD /app/start_services.sh