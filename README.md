# contact_box
Contact_box is an application written during the full-time bootcamp course. It enabled me to get to know better the django framework and work with the MySQL database. 

Application functionality is:

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

### 1.Virualenv

Create virtualenv for your project:

`$ virtualenv -p python3 contact_box`

### 2.Download

Now, you need the contact_box project files in your workspace:

`$ git clone https://github.com/dominikazdybek/contact_box.git && cd contact_box`
### 3.Requirements

To install all required dependencies, simply type:

`$ pip install -r requirements.txt`

You also need to download and install MySQL database (prefered version is 5.7) . You can get it from here: 

* https://dev.mysql.com/downloads

### 4.How to run

* `/manage.py migrate`

* `/manage.py runserver`






