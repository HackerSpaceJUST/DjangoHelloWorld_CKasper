# DjangoHelloWorld_CKasper

# Table of Contents
* [Table of Contents](#Table-of-Contents)
* [Overview](#overview)
* [Instructions](#instructions)
    * [How to create a Django project?](#How-to-create-a-Django-project)
    * [How to add a new app to Django project?](#How-to-add-a-new-app-to-Django-project)
    * [How to run Django server?](#How-to-run-Django-server)
    * [How to upload your work to your Repo?](#How-to-upload-your-work-to-your-Repo)

# Overview
This repo is for tracking my Django learning path.

# Instructions
## How to create a Django project?
```
django-admin startproject PROJECT_NAME
```

## How to add a new app to Django project?
```
python3 manage.py startapp APP_NAME
```

## How to run Django server?
```
python3 manage.py runserver
```

## How to upload your work to your Repo?
1. `git clone https://github.com/HackerSpaceJUST/<repo>`
1. Make a branch with a clear name for the feature you want to add: `git checkout -b BRANCH_NAME`. If the branch is already exist, then no need for the `-b` in the command.
1. Modify your changes on your local device.
1. When the modifications are finished: `git add .` to add all of the modified files.
1. Commit your work and write a clear message for your commit: `git commit -m "Your Message"`.
1. Push your work: `git push origin BRANCH_NAME`.
1. Go to `https://github.com/HackerSpaceJUST/<repo>`, add your commit as a pull request.
1. Go to Pull Requests and review your code.
1. If your changes got approved then merge it to the main branch.
1. Delete the used branch once the feature you're working on is finished.