# Use an official Python runtime as a parent image
FROM python:3.10 as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y default-mysql-client
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./

# Use a build argument to determine whether to install dev dependencies
ARG DEV
RUN if [ "$DEV" = "true" ] ; then pipenv install --system --deploy --dev ; else pipenv install --system --deploy ; fi

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
