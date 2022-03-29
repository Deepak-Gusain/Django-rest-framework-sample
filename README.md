# Django-rest-framework-sample
Django rest framework to read file and send response back.

1) This is the Django rest frame work which will receive post request and then it will send response.
2) We are using Authentication also, you have to create username and password pass it and you will get token. You have to use this token to send post request.
3) Run this code - "python3 manage.py runserver"
4) Use postman and send file with username and password. (url :- http://127.0.0.1:8000/api/login/)
5) You will get token and use this in postman (header) (Key:Authorization , Value:Token <token value>) --> (url :- http://127.0.0.1:8000/api/extract/)
6) We have enabled storage also.
  
If you want to run it in Docker container:-
  1) Create Docker file.
  2) Create requirement.txt.
  3) Use Gunicorn and Ngxin for prod.
  4) Allowed_host = ["*"] -- just for testing not for prod.
  5) Go to inside project folder and run - "docker build -t django_file_extraction ."
  6) After that you will get Docker image.
  7) Run it - "docker run -it -p 8000:8000 -e DJANGO_SUPERUSER_USERNAME=XXXX -e DJANGO_SUPERUSER_PASSWORD=XXXX -e DJANGO_SUPERUSER_EMAIL=XXXX django_file_extraction"
  
  Reference :- https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application
               top of view.py file.
