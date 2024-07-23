
from django.urls import path

from . import views

app_name = "content"
urlpatterns = [
    # ex: /exam/
     path("", views.load, name = "page"),
    # ex: /exam/result/
   
]