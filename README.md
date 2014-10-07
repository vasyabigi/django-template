### Install:

        $ django-admin.py startproject --template=https://github.com/vasyabigi/django-template/zipball/master  --extension py,md,gitignore,example woot

Where ``woot`` is the name of the project you'd like to create.


### Update README.md:

* Change repository link;
* Make `git add logs/.gitdirectory public/.gitdirectory static/.gitdirectory -f`;
* Remove everything above this sentence;

{{ project_name }}
========================================

## Installation ##

### Creating the environment ###
Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv {{ project_name }}
```

#### For virtualenv ####
```bash
virtualenv {{ project_name }}
source {{ project_name }}/bin/activate
```

### Clone the code ###

```bash
git clone YOUR-CUSTOM-REPO-LINK/{{ project_name }}.git
```

### Install requirements ###
```bash
cd {{ project_name }}
pip install -r reqs/dev.txt
```

### Configure project ###
```bash
cp settings/dev.py.example settings/dev.py
vi settings/dev.py
```

### Sync/migrate database ###
```bash
python manage.py migrate
```

## Running Django ##
```bash
python manage.py runserver
```
