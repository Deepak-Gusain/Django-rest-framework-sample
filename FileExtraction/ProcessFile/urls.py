from django.urls import path
from ProcessFile import views
from django.views.decorators.csrf import csrf_exempt
from .views import login, extract_json

urlpatterns = [
    path('api/login/', login),
    path('api/extract/', csrf_exempt(views.extract_json), name='extract_json'),

]