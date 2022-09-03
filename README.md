# AEAPI

Age Estimation API

# Description

Hello geeks,

Hmm, it's Saturday and I decided to learn django by building an API around my school project.

With my final year project, my project mate and I got to work on a research paper to prove upon an age estimation model.

Atm, I will give a more detail writeup for my project but today 03/09/2022, I decided why not have a mobile client to utilize the model. It's just sitting on my computer.

the model will be deployed to Heroku and the app will soon be developed. link to the app will be provided soon for y'all geeks

# How to run project server

first you'll need to install django, i prefer conda to manage my python envs and packages.

1. let's create virtual environment, you don't want conflicts with packages and python versions

you can use any other python modules to create a environment to work in.

> conda env create -n name

2. install django, django rest framework

> conda install django
> conda install djangorestframework

3. now let's run the server. change directory into root where manage.py is found

migrate database models to set it up

> python manage.py migrate

supersuser to handle administration stuff

> python manage.py createsuper

4. finally, run server

> python manage.py runserver

