
from django.urls import path

from . import views

app_name = "content"
urlpatterns = [
    # ex: /exam/
     path("", views.mainn, name = "main"),
     path("al/", views.load, name = "page"),
    # ex: /exam/result/
   
]