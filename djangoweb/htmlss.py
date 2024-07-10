from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def web1(request):
    y="(2, 'jeson', 'e', 'f', 'g', 'h', 'e')"
    x="Hhtfhrhr"
    dicta={
        "1":x,
        "two":y
    }
    return render(request, 'exam.html',  {'ti': y})
