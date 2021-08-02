# Project Template v1!

This is a template for a flask based web app which handles some basic user authentication and hosting configuration.

## What is included in the template

- README.md (this file)
- requirements.txt, a file that lists all the required modules
- a Python virtual environment
- User Authentication
- A database with a table for users
- A database migration framework
- Routes for user login views, and an empty index view
- HTML templates for all views
- A Procfile containing Heroku startup instructions
- 

## How to use this template

There are a number of places in this template where names of files and variables need to be changed before the app can be used for something else. 

### Things to change

#### Top level directory

- `project_template.py` needs to have its name changed to the name of your project
- `Procfile`, change project_template to the name of your project. This has to match the name of the python script in the top level
 
```web: flask db upgrade; gunicorn project_template:app```

- `config.py` needs to have the `SQLALCHEMY_DATEBASE_URI` changed to the production server


## Setting up Heroku

## App Design

The underlying architechture of this app is modelled after Miguel Grinberg's [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). Chapters 1-5 are required reading if you have no experience in Flask. There are also components of this app that follow examples from chapters 8, 11, 15, and 18.