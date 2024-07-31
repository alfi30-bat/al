
from django.urls import path

from . import views

app_name = "exam"
urlpatterns = [
    # ex: /exam/
    path("", views.exampage, name = "exam"),

    # ex: /exam/result/
    path("result/", views.answerpage, name = "anspage"),
    #path("score/", views.core, name = "sco"),
    path("detailed/", views.danswerpage, name = "danss"),
   
]