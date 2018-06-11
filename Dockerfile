FROM python:latest 

RUN apt-get update && apt-get install -y \
	gettext

EXPOSE 8000

COPY config/python/requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY src /srv

WORKDIR /srv

RUN chmod +x start.sh

ENTRYPOINT [ "./start.sh" ]