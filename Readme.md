# Instagram
#### Web clone of the Instagram app
#### March 11th, 2019
#### By **[James Mwangi](https://github.com/jamesnduge)**

## Description
This is a simple web clone of the instagram website. A user can create an account and sign into it. 
The site supports uploading images, and following other users. 
users can view photos uploaded by other users in the home page of app.

## Behaviour Driven Development
|Behaviour| Input | Output|
|---------|-------|-------|
|Homepage| - | -
|user clicks on  image| clicks image  | image information page opens
|user clicks on like | click like button | like count is incremented
|user click on search bar in navbar| click search| searches for various users in the application

## Set Up and Installation

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/Jamesnduge/Insta.git && cd Insta`

### Activate virtual environment
Activate virtual environment using python3.7 as default handler
```bash
python3.7 -m venv --without-pip virtual && source virtual/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

### Create the Database
```bash
psql
CREATE DATABASE insta;
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'insta'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'
```
### Run initial Migration
```bash
python3.6 manage.py makemigrations gram
python3.6 manage.py migrate
```

### Run the app
```bash
python3.7 manage.py runserver
```
Open terminal on `localhost:8000`

## Technologies used
    - Python 3.7.2
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details
Contact me on james_mwangi@aol.com for any comments, reviews or advice.