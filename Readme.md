#Blog Website


Steps to run project

1) To apply migrations
  -Run python manage.py migrate
  
2) To create a superuser
  -Run python manage.py createsuperuser

3) Start the Django development server.
 - Run python manage.py runserver
  
4) Access the Admin Panel:
- Go to http://127.0.0.1:8000/admin/

5) Access the APIs:
 - Go to http://127.0.0.1:8000/blog/list/
 - Go to http://127.0.0.1:8000/blog/create/
 - Go to http://127.0.0.1:8000/blog/<post_id>/create-comment/
 - Go to http://127.0.0.1:8000/blog/<post_id>/update/
 - Go to http://127.0.0.1:8000/users/login
 - Go to http://127.0.0.1:8000/users/logout