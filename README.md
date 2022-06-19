# Green Miles

Submission for Grab Hackathon 2022

## Getting Started

First, please make sure you have following prerequisites on your machine

### Pre requisites
1. Install docker in your laptop
2. Install PostgreSQL in any of your machine


### How To
You need to install all the dependencies in order the project can run on your local.
1. Clone repo into your machine
2. Create database in your PostGreSQL i.e : greenmiles
3. Import file `greenmiles.sql` into your created DB 
4. Make .env file with the following path project/project/settings/.env . 

```
README.md
docker
project
│   rest_admin
│   rest_api
│   vendor
|   manage.py
└───project
    │   urls.py
    │   wsgi.py
    │   __init__.py
    └───settings
        │   __init__.py
        │   staging.py
        │   base.py
        │   .env
```
5. In the .env file , put DB configuration like below example

```
DB_NAME=greenmiles
DB_USER=yourdatabaseusername
DB_PASSWORD=yourpassword
DB_HOST=127.0.0.1
DB_PORT=5432
DEBUG=1
DJANGO_ENV=staging
```
6. Go to your root folder of the greenmiles project, 

```
cd /your-machine-directory/greenmiles-api
```
7. In the root folder, run following command
```
sh docker/bin/deploy.sh 
```

8. Your service will be run at 
```
http://localhost:7302
``` 