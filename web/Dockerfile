# Use an official Python runtime as a parent image
FROM python:3.10 as builder

# Set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y default-mysql-client
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

COPY . .
COPY .env .env

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
