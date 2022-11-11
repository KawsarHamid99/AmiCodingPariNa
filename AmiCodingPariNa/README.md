# installation 
-install DjangoRestFrameWork

###### _A Django Project._

# __Template features:__
- User Model with Profile
- Django REST Framework with API endpoints and view sets


# __Usage:__
> _This document will be using the following as an input variable: `<variable>`. Please input your own value, i.e. `<project_name>` --> My-Project_
>
> _Please make sure `git`, `python`, `django` and `rest_framework` is installed in the system._
>


1. ### Prepare project directory
    - Make your project directory (must be the same name as your github repository name)
    - Work from the project directory as current directory using `cd`.
    - Create a virtual environment using `python`. (Test via `python -V`. )
    - `Activate` the virtual environment. (Windows: `source venv/Scripts/activate`)
    - Install `Django` using `pip`.
    - Install `djangorestframework` using `pip`.
    ```shell script
    mkdir <project_name> && cd $_
    python -m venv venv
    source venv/bin/activate
    # Windows: source venv/Scripts/activate
    python -m pip install --upgrade pip
    ```

2. ### Install Django and startproject
    - Install `Django` v3 using `pip` within your `venv`
    - Download the Project form github
    - Start your project using `django-admin` and the template.
    ```shell script
    pip install django
    pip install djangorestframework
    pip install requests
    # download the template.zip linked above
    django-admin startproject \
        
    ```
    > _NOTE: `<project_name>` must be the exact same name as your project repository name. The period `.` at the end of `django-admin` starts the project in the current directory._

3. ### Create Database and User
    sqlite database has been used here

4. ### Configure the project
    

5. ### Run the project
    - Run `makemigrations` and `migrate`.
    - Run `tests` and `linting` to assure nothing is broken.
    - Create superuser to access the admin panel.
    - Run django `server` to view the project or application.
    - Generate `coverage` reports locally.
    ```shell script
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    
  
    
    
