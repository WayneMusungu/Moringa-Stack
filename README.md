# MORINGA-STACK

#### By Wayne Musungu, Edah Chepngetich, Victor Makori, Haimana Uta, Clinton Wambungu and James Musembi

### It is a description of my resume.

## Table of Content

- [Description](#Description)
- [Installation Requirement](#Installation)
- [Technologies Used](#Technologies-Used)
- [Reference](#Reference)
- [Licence](#LICENSE)
- [Authors Info](#Author-Info)

## Description

Moringa-stack allow you to access to qualitatives and very well curated batch of answers. First of all, it allows you to filter answers who fit with your points of interest by choosing Watched/Ignored Tags. An other useful thing is to filter questions/answers by popularity (upvotes/downvotes)

#### Technologies used
    - Python 3.8
    - HTML
    - CSS
    - Bootstrap 5
    - Heroku
    - Postgresql
    - Django, Django Rest Framework

[Go Back to the top](#MORINGA-STACK)

# Installation

### Requirements

Either a computer,phone,tablet or an Ipad
Make sure you have access to internet
Click on the live link in the about section 

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Create the Database
In a new terminal, open the postgresql shell with `psql`.
```bash
CREATE DATABASE moringastackers; 
```

#### Make and run migrations
```bash
python3.8 manage.py makemigrations && python3.8 manage.py migrate
```

#### Run the app
```bash
python3.8 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)

## Running the tests

Run test using the following command


```
 ./manage.py test moringastackers
```

[Go Back to the top](#MORINGA-STACK)


