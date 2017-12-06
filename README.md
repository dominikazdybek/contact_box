# contact_box
Contact_box is an application written during the full-time bootcamp course. It enabled me to get to know better the django framework and work with the MySQL database. 

Application functionalities is:

* storing list of contacts
* adding, editing, deleting contact
* storing groups
* adding, editing, deleting group
* adding contact to group
* finding members in group
* deleting contact from group

## Stack

* Python 3.5
* Django 1.11
* MySQL 
* HTML + CSS (Bootstrap)

## How to build the project locally

### 1. Download

You need the contact_box project files in your workspace:

`$ git clone https://github.com/dominikazdybek/contact_box.git`

### 2. Virualenv

Create virtualenv for your project and activate it:

`$ virtualenv -p python3 contact_box_env`

`$ source contact_box_env/bin/activate`

### 3. Requirements

Download and install MySQL database (prefered version is 5.7). You can get it from here: 

* https://dev.mysql.com/downloads

To install all required dependencies, simply type:

`$ cd contact_box`

`$ pip install -r requirements.txt`

### 4. How to run?

First, create database called `contact_list` in MySQL. Then define your credentials in settings file: `warsztat_3_contact_list/settings.py`.

Make migration:

* `/manage.py migrate`

Run server:

* `/manage.py runserver`






