# Project Setup Guide

This guide will help you get started with setting up the project on your local machine. Follow the steps below to clone the repository, install dependencies, configure the database, and run the server.

## 1. Clone the Repository

First, clone the repository to your local machine using the following command:

```
git clone "https://github.com/akash2704/ResumeProcessor"
```
## 2. Install dependencies
 ```
 pip install -r requirements.txt
 ```
## 3. Configure PostgreSQL.
In `ResumeProcessor/settings.py`, configure the database settings:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'resume_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
## 4. Run migrations:
```
pyhton manage.py makemigrations
```
```
python manage.py migrate
```
## 5. Start the server:
```
python manage.py runserver
```
