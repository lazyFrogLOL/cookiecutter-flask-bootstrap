FROM python:3.6

RUN adduser {{cookiecutter.app_name}}

WORKDIR /home/{{cookiecutter.app_name}}

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY {{cookiecutter.app_name}} {{cookiecutter.app_name}}
COPY migrations migrations
COPY {{cookiecutter.app_name}}.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP {{cookiecutter.app_name}}.py

RUN chown -R {{cookiecutter.app_name}}:{{cookiecutter.app_name}} ./
USER {{cookiecutter.app_name}}

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]