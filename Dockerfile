# This file is a template, and might need editing before it works on your project.
FROM python:3.9.2

# Edit with mysql-client, postgresql-client, sqlite3, etc. for your needs.
# Or delete entirely if not needed.
RUN apt-get update \ 
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

RUN apt-get install gcc

COPY requirements.txt /usr/src/app/
RUN pip install --upgrade pip setuptools wheel gunicorn
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app

# For Django
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# For some other command
# CMD ["python", "app.py"]
