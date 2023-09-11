FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/project/rockstore

COPY ./requirements.txt /usr/project/requirements.txt

RUN pip3 install -r /usr/project/requirements.txt

COPY . /usr/project/rockstore

EXPOSE 8000

#CMD ["python3", "manage.py", "makemigrations"]
#CMD ["python3", "manage.py", "migrate"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
