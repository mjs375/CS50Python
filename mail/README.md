
$ python3 manage.py createsuperuser
  - *create an admin account (url-path/admin)*

$ python3 manage.py makemigrations mailbox
$ python3 manage.py migrate
  - *anytime you make changes to models.py, run the above code to incorporate the changes.*

$ python3 manage.py runserver
  - *run/open the web application*
