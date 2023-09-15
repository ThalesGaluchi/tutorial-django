
# Tutorial para *django*

Referencias
https://docs.djangoproject.com/en/4.2/topics/install/#installing-official-release


a) Criar ambiente virtual (https://docs.djangoproject.com/en/4.2/intro/contributing/)
>>python3 -m venv <
>>source <nome>/bin/activate

Remover environment: 
Linux 
>>rm -rf env/

Windows 
>>rmdir ourenv /s /q

b) Update pip
>> python -m pip install --upgrade pip

c) Install Django
>>python -m pip install Django

***Alternative:***
Install pipenv
>>pip install pipenv

Create project folder
>> mkdir <foldername>
>> cd <foldername>

Install pipenv
>> pipenv install django
-> Pipfile file is created

In VS terminal
>> pipenv --venv

Ctrl+Shift+P > Select Virtual environment> enter interpreter path...
/home/thales/.local/share/virtualenvs/tutorial-django-ji_-FTkZ + /bin/python

Terminal
Activate environment
>>source /home/thales/.local/share/virtualenvs/tutorial-django-ji_-FTkZ/bin/activate

>> python manage.py runserver


## Django tutorial app

Create a basic poll application:

It’ll consist of two parts:
* A public site that lets people view polls and vote in them.
* An admin site that lets you add, change, and delete polls.

https://docs.djangoproject.com/en/4.2/intro/tutorial01/


1) Verify django version:
>>python -m django --version
The tutorial works for Django 4.2+ and Python 3.8+

2) Create a Project:
>>django-admin startproject mysite

- Create 'mysite' folder with the files.

*** Place the code in some directory outside the root (/home/myproject)
** Do not use words as **django** or **test** (python) to avoid conflicts

mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py


3) Test installation

>> cd <nome>
>>python manage.py runserver

Options:
Change server port  >>python manage.py runserver 8080
Change IP:port >>python manage.py runserver 0.0.0.0:8080

3) Create the Polls app

a) in the same folder of 'manage.py' type:
>> python manage.py startapp polls

A 'pools' folder is created.

polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py


4) Write first view

a) Code in views.py
b) create polls/urls.py
c) point root URLconf at polls.urls module in mysite/urls.py
d) test >> python manage.py runserver
(url: http://localhost:8000/polls/)

***include() is used to include other URL patterns

The path() function is passed four arguments, two required: **route** and **view**, and two optional: **kwargs**, and **name**.
**route**: strng that contains URL pattern
**view**: when Django finds the matching pattern it calls the specified function with HttpRequest object
**kwargs**: arbitrary keywords argumens
**name**: refer to it unambiguously from elsewhere Django

PART 2

5) Database setup

<nome>/settings.py

It come with *SQLite* configured. For other databases, change **DATABASES** field.
*ENGINE* : 'django.db.backends.mysql' or 'django.db.backends.postgresql'
*NAME* : database name
For external DB, use *USER*, *PASSWORD*, *HOST*


6) Installed Apps

By default, INSTALLED_APPS contains the following apps, all of which come with Django:

django.contrib.admin – The admin site. You’ll use it shortly.
django.contrib.auth – An authentication system.
django.contrib.contenttypes – A framework for content types.
django.contrib.sessions – A session framework.
django.contrib.messages – A messaging framework.
django.contrib.staticfiles – A framework for managing static files.

Some of these applications make use of at least one database table, though, so we need to create the tables in the database before we can use them. To do that, run the following command:

>>python manage.py migrate

<<<< Part 2 >>>>

7) Creating Models

Models are database layouts with additional metadata. Model is the single source of information about the data. Django follows DRY Principla (Don't Repeat Yourself)

In this tutorial  the models as:
* **Question**: a question and puplication date
* **Choice**: the text of the choice and vote tally.

Each **Choice** is associated to a **Question**.
'polls/models.py'

<good explanationin tutorial>

8) Activating models

That small bit of model code gives Django a lot of information. With it, Django is able to:

Create a database schema (CREATE TABLE statements) for this app.
Create a Python database-access API for accessing Question and Choice objects.
But first we need to tell our project that the polls app is installed.

add to <name>/settings.py => "polls.apps.PollsConfig" to *INSTALLED_APPS*

Then we include the app to our project.

>>python manage.py makemigrations polls

*OBS.* 'makemigrations' tells Django about changes in the models that we wanto to store as migration. They are stores in "polls/migrations" folder

>> python manage.py sqlmigrate polls 0001

Note the following:

The exact output will vary depending on the database you are using. The example above is generated for PostgreSQL.
Table names are automatically generated by combining the name of the app (polls) and the lowercase name of the model – question and choice. (You can override this behavior.)
Primary keys (IDs) are added automatically. (You can override this, too.)
By convention, Django appends "_id" to the foreign key field name. (Yes, you can override this, as well.)
The foreign key relationship is made explicit by a FOREIGN KEY constraint. Don’t worry about the DEFERRABLE parts; it’s telling PostgreSQL to not enforce the foreign key until the end of the transaction.
It’s tailored to the database you’re using, so database-specific field types such as auto_increment (MySQL), bigint PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY (PostgreSQL), or integer primary key autoincrement (SQLite) are handled for you automatically. Same goes for the quoting of field names – e.g., using double quotes or single quotes.
The sqlmigrate command doesn’t actually run the migration on your database - instead, it prints it to the screen so that you can see what SQL Django thinks is required. It’s useful for checking what Django is going to do or if you have database administrators who require SQL scripts for changes.

NOW run the migrate
>>python manage.py migrate

remember the three-step guide to making model changes:

Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.
The reason that there are separate commands to make and apply migrations is because you’ll commit migrations to your version control system and ship them with your app; they not only make your development easier, they’re also usable by other developers and in production.



8) Play with the app

>>python manage.py shell

(...)

Add *__str__(self)* methods within the objects

__ to follow relationship

9) Create admn user

>>python manage.py createsuperuser

adm
adm@abc.com
biscoito

run the app
>> python manage.py runserver
http://127.0.0.1:8000/admin/


10) Make the pool app editable by admin

polls/admin.py

Allow admin to edit question.
Play around on the site.

<<< Part 3 >>>

A view is a “type” of web page in your Django application that generally serves a specific function and has a specific template. 
A URL pattern is the general form of a URL - for example: /newsarchive/<year>/<month>/.
To get from a URL to a view, Django uses what are known as ‘URLconfs’. A URLconf maps URL patterns to views.

11) Create more VIEWS

Add views at polls/views. - add a function for each view
Wire them at polls.urls adding path() calls

We write in the browser: "../polls/34"
- system goes to polls.urls.py (Because it is pointed by **ROOT_URLCONF** in *settings.py*)
- find *path('<int:question_id>/, views.detail) [variablename urlpatterns]
- run detail() from "polls/views.py", that returns a *HttpResponse(response % question)*


12) Write views that works

Each view must return an HttpResponse or Http404.
Then, the view can do whatever we want.

Create folder \templates\polls in polls
- File index.html

render() in view.py

13) Raise 404 error

polls/views > function detail()

14) Use the template system

Uses dot-lookup syntax

question.question_text: lookup in object question, then attribute question_text

or question.choice_set.all: returns an iterable of Choice


15) Remove hardcoded URL in templates  **** Parei aqui

To remove the hardcoded '/polls/', we set name argument in path() [inside polls.urls]. It looks for the 'name' == {% url 'detail' ... }

16) Namespacing URL names

Used to diferenciate the apps in the project

- add app_name in polls/urls.py
- change polls/index.html
== {% url 'polls:detail' ... }

<< Part 4 >>

CONTINUE
https://docs.djangoproject.com/en/4.2/intro/tutorial04/

4.1) A minimal Form in question polls/detail.html


4.2) Use generic views: Less code is better

We can convert our poll app to use generic views system:
a) Convert the URLconf
b) Delete some ols unneeded view
c) Introduce new views based on Django's generic views

4.2.1) Amend URLconf

polls/urls.py

Amened views
 polls/views.py

- each generic view requires a model to be action on
- the DetailView expects the primary key value captures from the URL to be called 'pk'. then it was changed the 'question_id" to 'pk'.

standard: <app_name>/<model_name>_list.html
template_name changes this standard for list, detail and results pages.

in ListView, the 'context_object_name' overrides the standat pattern <model_name>_list.html



<<< Part 5 >>>


## Introducing automated tests?

Good text about the importance of automate tests

5.1) Write first test

Check the publication date is in the future.
>>python manage.py shell
(use the code in polls/tests.py in the shell)

OR
Using 'polls/tests.py'
>> python manage.py test polls

What happened is this:

manage.py test polls looked for tests in the polls application
it found a subclass of the django.test.TestCase class
it created a special database for the purpose of testing
it looked for test methods - ones whose names begin with test
in test_was_published_recently_with_future_question it created a Question instance whose pub_date field is 30 days in the future
… and using the assertIs() method, it discovered that its was_published_recently() returns True, though we wanted it to return False
The test informs us which test failed and even the line on which the failure occurred.

5.2) Fix the bug in 'polls/models.py'


5.3) Django test client

Used to test the views.

>> python manage.py shell

>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()

setup_test_environment() installs a template renderer which will allow us to examine some additional attributes on responses such as response.context that otherwise wouldn’t be available. **Note that this method does not set up a test database**, so the following will be run against the existing database and the output may differ slightly depending on what questions you already created. You might get unexpected results if your TIME_ZONE in settings.py isn’t correct. If you don’t remember setting it earlier, check it before continuing.

Tests are ran in shell

5.4) Improve our view

Lots of code in polls/tests.py
run the test to past and future questions.

First is a question shortcut function, create_question, to take some repetition out of the process of creating questions.

test_no_questions doesn’t create any questions, but checks the message: “No polls are available.” and verifies the latest_question_list is empty. Note that the django.test.TestCase class provides some additional assertion methods. In these examples, we use assertContains() and assertQuerySetEqual().

*In test_past_question, we create a question and verify that it appears in the list.

In test_future_question, we create a question with a pub_date in the future. The database is reset for each test method, so the first question is no longer there, and so again the index shouldn’t have any questions in it.*

5.5) Testing the DetailView



5.6) Testing: the more the better

As long as your tests are sensibly arranged, they won’t become unmanageable. Good rules-of-thumb include having:

- a separate TestClass for each model or view
- a separate test method for each set of conditions you want to test
- test method names that describe their function

more at: https://docs.djangoproject.com/en/4.2/topics/testing/

https://docs.djangoproject.com/en/4.2/topics/testing/advanced/#topics-testing-code-coverage

## Part 6

6.1) Add stylesheet and image

django.contrib.staticfiles

6.2) Customize look and feel

Create a directoty **static** in **polls** directory.

6.3) Add background image

This is the very basic. Check for more in specific pages.
https://docs.djangoproject.com/en/4.2/howto/static-files/

https://docs.djangoproject.com/en/4.2/howto/static-files/deployment/

## Part 7

7.1) Customize the admin form

using the 'adimin.py' file

7.2) Adding related objects


7.3) Customize the admin change list

7.4) Customize the admin look and feel
Create 'template' folder in project directory

>> python -c "import django; print(django.__path__)"
['/home/thales/.local/share/virtualenvs/tutorial-django-ji_-FTkZ/lib/python3.10/site-packages/django'] + contrib/admin/templates/admin/base_site.html


Copy base_dir.html to the created folder

https://docs.djangoproject.com/en/4.2/topics/templates/#template-loading

## Part 8

https://docs.djangoproject.com/en/4.2/intro/tutorial08/

8.1) Using 3rd party packages

**Django Debug Toolbar**

>> python -m pip install django-debug-toolbar

https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

https://docs.djangoproject.com/en/4.2/intro/reusable-apps/

--extras--

https://adamj.eu/tech/2021/11/04/the-well-maintained-test/


https://docs.djangoproject.com/en/4.2/intro/whatsnext/