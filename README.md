##########
Django CMS
##########
# Content Management System API + User Model
---
This is CMS api built using Python Django Rest Framework to demonstrate API operations,groups and permissions.This API allow user-author to Create,Update,Delete content of their own and list all content of
other users-authors (Author Group).Admin has explicit access to all content and permission through Admin Group.
---

### Getting Started
---
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Programming Language and Frameowork
---
* Python
* Django REST framework

### Version Used
---
* Python: 3.7.3
* Django: 3.1.1
* DjangoRESTframework: 3.11.1


***********
Quick Start
***********
#. Clone or Download this repo. Then follow these instructuons. -
	$ git clone "git hub project link"

#. Create a Python 3.6 virtualenv

    $ virtualenv env
    $ source env/bin/activate

### Library Used
---
**P.S**:*For installation of required library or modules refer [requirement.txt](https://bitbucket.org/decimal-point-analytics/mahindra_robopulse_api/src/fa14e45626d772e30c228219dc0038aa0f4c5f4b/requirements.txt?at=feature%2Ft1000) file and directly install using following command*

	(env) $ pip install -r requirements.txt
    (env) $ python manage.py runserver
	(env) $ python manage.py makemigrations
	(env) $ python manage.py migrate

### Project Description
---
This project has api's created to perform crud oeprations in content management.
Following are the apps created under this project.

* **USER**: Extended build in model to add extra fields
* **API**: This is core app where api's are developed.

### Instruction
---
Create Superuser
Add Groups 'Admin Group' and 'Author Group'
Assign User to this groups from Django Admin
Then can add data from post request and test other functionalities with urls

### Data Source
---
* sqlite3 database


## Built With

* [Django Rest Framework](https://www.django-rest-framework.org) - The web framework used


## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change.
Please note we have a code of conduct, please follow it in all your interactions with the project.


## Authors

* **Developers**: Pratik Nikam


