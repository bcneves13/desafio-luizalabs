FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /django_code
WORKDIR /django_code
COPY requirements.txt /django_code/
RUN pip install -r requirements.txt
COPY . /django_code/