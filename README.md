# Django File Uploader

This is a program that allows you to upload files with their lifetime.

The next options are available:
- view files list;
- check the remaining lifetime of the file;
- delete the file before the expiration of the file

You can check the project here: [filesharing-2019](https://filesharing-2019.herokuapp.com/)

## Running the Project Locally

First, clone the repository to your local machine:

`$ git clone https://github.com/Mazzart/esl_19_1.git`

Install the requirements:

`$ pip install -r requirements.txt`

Apply the migrations:

`$ python manage.py migrate`

Finally, run the development server:

`$ python manage.py runserver`

The project will be available at **http://127.0.0.1:8000/**