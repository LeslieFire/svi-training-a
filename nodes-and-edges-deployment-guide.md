#Nodes and Edges App Deployment

###AWS Instance
1. First create an AWS instance.
2. save the pem key to /home/your_username/.ssh/
3. edit the inbound security rules under Security Groups dropdown to include HTTP with port range 80. This is so you can access the instance from the net.
4. change the security of the key using: ```chmod 400 name_of_key_pair.pem```

###Getting inside the terminal
for ubuntu virtual instance:
* To get inside the instance, you can use the public ip: ```ssh -i name_of_key_pair.pem ubuntu@public_ip```
* or you can use the public dns: ```ssh -i name_of_key_pair.pem ubuntu@public_dns```

To transfer files inside, use: ```scp -i name_of_key_pair.pem samplefile.txt ubuntu@public_ip:<path within instance>```

To transfer folders, replace **samplefile.txt** with ```-r path/to/folder``` -r for recursive transfer.

###Updating the system instance
Inside the instance, make sure to run commands below so that everything gets updated before we begin our work:
* ```sudo apt-get update && sudo apt-get upgrade```

###Install/Setup PostgreSQL
link guide: [https://help.ubuntu.com/community/PostgreSQL](https://help.ubuntu.com/community/PostgreSQL)

Install postgres: ``` sudo apt-get install postgresql postgresql-contrib```

To start off, we need to change the PostgreSQL postgres user password; we will not be able to access the server otherwise. As the “postgres” Linux user, we will execute the psql command.

1. On the terminal, type ```sudo -u postgres psql postgres```
2. Set a password for the "postgres" database role using the command: ```\password postgres```
3. To create your db with "postgres" as the user: ```sudo -u postgres createdb name_of_db```

However, you still wouldn't be able to directly ```psql``` directly to the terminal. To change that:

1. create a superuser that has the same name as your current ubuntu user: ```sudo -u postgres createuser --superuser $USER```
2. access psql: ```sudo -u postgres psql```
3. inside psql, to change password of current user: ```\password <the name of the the user>```
4. to quit psql ```\q```
5. outside psql, to create the db: ``` sudo -u $USER createdb $USER```

Connecting to your own database should be as easy as ```psql``` now.
* creating other db will now be like: ``` createdb amarokdb;```

To access gain access on a local database without it asking for username and password:

1. access the **pg_hba.conf** file:  ```sudo nano /etc/postgresql/9.3/main/pg_hba.conf``
2. change the line:
```
# Database administrative login by Unix domain socket
local   all             postgres                                peer
```
to
```
# Database administrative login by Unix domain socket
local   all             postgres                                trust
```
&nbsp;&nbsp;3. &nbsp;reload postgreSQL server configuration: ```sudo /etc/init.d/postgresql reload```

###Install pip/virtualenv/virtualenvwrapper
Install pip (for easy module installation): ```sudo apt-get install python-pip```

Install virtualenv (for easy dependency management): ```sudo pip install virtualenv```

Install virtualenvwrapper (for easier dependency management): ```sudo pip install virtualenvwrapper```

To make virtualenvwrapper work, place the following lines at ~/.bashrc:
```
export PATH=/usr/local/bin:$PATH
source /usr/local/bin/virtualenvwrapper.sh
```
Then reload ~/.bashrc: ```. ~/.bashrc```

Install python-dev (needed by psycopg2): ```sudo apt-get install python-dev```

Install python-dev (to make **psycopg2** work which is then used by **sqlalchemy**): ```sudo apt-get install libpq-dev``` and ```sudo pip install psycopg2``` 

###Transferring the Nodes and Edges repo from github to the instance.

create a virtualenv for all the dependencies: ```mkvirtualenv nae_1 && workon nae_1```

Install git: ```sudo apt-get install git```

On ```~```: ```git clone https://github.com/SiliconValleyInsight/nodes-and-edges.git```

Inside the nodes-and-edges folder, switch to the most updated branch: ```git checkout anton_branch10/code_refactoring```

populate virtualenv with dependencies: ```pip install -r requirements.txt```

Check if everything is running by running the tests again (if ever you created a few).

###Setting up NGINX
Installing nginx: ```sudo apt-get install nginx```

Delete the default config and create a new config for the app that will listen to port 80 (the HTTP port that we set while creating the AWS instance) and will then pass it to port 8000 (the default port of gunicorn):

```sudo rm /etc/nginx/sites-enabled/default```

```sudo nano /etc/nginx/sites-available/flask_project```

Inside the flask project, write:
```
  server {
    listen 80;
    server_name example.org;
    access_log  /var/log/nginx/example.log;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
  }
```
Create a symbolic link to sites enabled: ```sudo ln -s /etc/nginx/sites-available/flask_project /etc/nginx/sites-enabled/flask_project```

Restart nginx to start the new changes with either method:
* ```sudo /etc/init.d/nginx restart```
* ```sudo service nginx restart```

###Creating a Gunicorn Script for Supervisor
In production, we won't be running a single threaded development servers. We will instead use a dedicated application server called **gunicorn**.

A better way to run gunicorn is from bash script. That way it can easily be run by Supervsior:


create a text file inside ```nodes-and-edges/scripts/``` : ```nano local_gunicorn_start```
```
#!/bin/bash

NAME="gunicorn_nae"                                                                     # name of the application
FLASKDIR=/home/ubuntu/nodes-and-edges                                                   # flask project directory
USER=ubuntu                                                                             # the user to run as
NUM_WORKERS=3                                                                           # how many worker processes should Gunicorn spawn
FLASK_WSGI_MODULE=run                                                                   # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
# Do not use virtualenvwrapper inside here. It will keep on looking for\
# the virtualenv folder at main root folder of linux and not inside /home.
source /home/ubuntu/.virtualenvs/nae_1/bin/activate

# Start the Green Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
cd $FLASKDIR

# KEYS for stripe
# These currently has no use as we're not using Stripe yet. And even then, these credentials should be inside local_config.ini instead.
export PUBLISHABLE_KEY=<create your own keys on stripe>
export SECRET_KEY=<create your own keys on stripe>

gunicorn ${FLASK_WSGI_MODULE}:app \
    --name $NAME \
    --workers $NUM_WORKERS \
    --log-level=info \
    --log-file=-
```

test if its working by running: ```./local_gunicorn_start```

###Creating Celery Run Script for Supervisor

Install the preferred message broker ```sudo apt-get install rabbitmq-server```

Our celery config is located inside ```/nodes-and-edges/scrape/celeryconfig.py```

The tasks are located inside ```/nodes-and-edges/scrape/tasks.py

Create a script inside ```/nodes-and-edges/scripts```: ```nano local_celery_script```
```
#!/bin/bash

NAME="celery_nae"
FLASKDIR=/home/ubuntu/nodes-and-edges
USER=ubuntu

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
# Do not use virtualenvwrapper inside here. It will keep on looking for\
# the virtualenv folder at main root folder of linux and not inside /home.
source /home/ubuntu/.virtualenvs/nae_1/bin/activate

# Start Celery
cd $FLASKDIR

celery -A scrape.tasks worker --loglevel=info --beat -n worker.%h
```
###Setting up S3

1. Create a bucket on your S3 account.
2. on the permissions, add yourself as grantee and then check all the permission boxes
3. On the Edit Bucket Policy section, add:
```
{
	"Version": "2012-10-17",
	"Id": "Policy1442301995991",
	"Statement": [
		{
			"Sid": "Stmt1442301993891",
			"Effect": "Allow",
			"Principal": "*",
			"Action": "s3:GetObject",
			"Resource": "arn:aws:s3:::svi-nodes-and-edges-bucket/*"
		}
	]
}
```
This is to allow the public to access the image url's from s3

###Configure local_config.ini
add a local_config file in the root folder ```~/nodes-and-edges/```: ```nano local_config.ini```
```
[env]
debug = true
testing = false
static_path = /home/ubuntu/nodes-and-edges/static/logos

[s3]
user = AKIAI4ZGNAF5UPHXXNVQ
password = BmptssKZHU+XBldiLkb1TGW1K2nszip/qLJPrOrD
bucket_name = svi-nodes-and-edges-bucket
origin_path = /static/logos

[flask]
wtf_csrf_enabled = false
jsonify_prettyprint_regular = false
secret_key = i0hFEJBqikeYUx6eH1gclnA1q1wav95x3NBaBRVFXKqyxLIjlTZBm7iWi38PDbNL
session_cookie_httponly = true
session_cookie_secure = false

[api]
version = 0.0

[db]
username =
password =
name = nodes_and_edges
url = postgresql+psycopg2://localhost/nodes_and_edges
engine_args_literal = {
    'pool_size': 10,
    'max_overflow': 0,
    'pool_recycle': 3600,
    'echo': False,
    'client_encoding': 'utf8'
  }
```
These includes all the urls, names, and credentials needed for the app to run.

###Setup Nodes and Edges Flask App
Make sure you are at ```/nodes-and-edges/``` root folder and youre inside the virtualenv ```nae_1```

1. Create db: ```createdb nodes-and-edges```
2. install the app in the virtualenv: ```python setup.py develop```
3. run migration scripts: ```./scripts/db_upgrade.sh```

if you want to test it on your local: ```python run.py --develop```

if you want to create migration on db upgrads: ```alembic -c backend/alembic.ini revision --autogenerate -m "create user table"```

###Running Tests
1. install tox ```pip install tox```
2. Create databases for the tests: ```createdb flask_api_template``` ```createdb flask_api_template_skeleton```
3. to run tox, just type: ```tox``` at the terminal

We currently have 3 tests: pylint, pep8, and tests. To run these indivually: ```tox -e pylint```, ```tox -e pep8```, or ```tox -e tests```

###Using Supervisor to daemonize tasks
We will be using Supervisor to automate processes and running on the background.

To install Supervisor: ```sudo apt-get install supervisor```

to create a configuration file: ```sudo nano /etc/supervisor/conf.d/nae_project.conf```

Include the commands that are supposed to be ran inside the conf file:
```
[program:gunicorn]
command = /home/ubuntu/nodes-and-edges/scripts/local_gunicorn_start                   ; Calling the start app
stdout_logfile = /home/ubuntu/nodes-and-edges/logs/gunicorn_supervisor.log            ; Where to write log.
redirect_stderr = true                                                                ; Set to True so that errors will still be logged
user = ubuntu                                                                         ; User to run as.

[program:celery]
command = /home/ubuntu/nodes-and-edges/scripts/local_celery_start
stdout_logfile = /home/ubuntu/nodes-and-edges/logs/celery_supervisor.log
redirect_stderr = true
user = ubuntu
```
Create the log files. At ```~/nodes-and-edges/logs/```: ```touch > celery_supervisor.log```, ```touch > gunicorn_supervisor.log```

To check if the config have changed: ```sudo supervisorctl reread```
to run the update of the project (and then running them): ```sudo suprvisorctl update```

Now that we have set up everything, lets run the app!: ```sudo supervisorctl start all```

Commands to on running supervisor:
- to check the status: ```sudo supervisorctl status gunicon```
- to stop: ```sudo supervisorctl stop gunicorn```
- to start: ```sudo supervisorctl start gunicorn```
- to check everything: ```sudo supervisorctl start all```

###Setting up the Linkedin Accounts that will be used.
To get the info that we need on accessing Linkedin in, we would have to be logged in and for us to be logged in, we need authenticated users first. I have already created two.
