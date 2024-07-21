from django.shortcuts import render, get_object_or_404
import sqlite3, random
from random import randint
from .models import phy_easy


from django.db.models import Count
# Create your views here.
def exampage(request):
    i=1
    # Iterate through the dictionary and add each item to the array
    #row = phy_easy.objects.get(id=1)
    count = phy_easy.objects.aggregate(count=Count('id'))['count']
    random_index = randint(0, count - 1)
    print(phy_easy.objects.all()[random_index])
    x=[]
    k=0
    while i<3:
        random_index = randint(0, count - 1) 
        if random_index==k:
            random_index = randint(0, count - 1) 

        k=random_index
        print("not equal")
        row = phy_easy.objects.all()[random_index]
        print(row.question)
        x.append(row.question)
        x.append(row.option1)
        x.append(row.option2)
        x.append(row.option3)
        x.append(row.option4)
        x.append(row.answer)
        i=i+1    
    print(x)
    x=str(x)
    x=x.replace("['", "")
    x=x.replace("']", "")
    #x="jeson', 'e', 'f', 'g', 'h', 'e', 'alfred', 'a', 'b', 'c', 'd', 'd', 'alfredoooo', 'aa', 'ba', 'cc', 'dd', 'cc', 'jesonnnnnn', 'e', 'ff', 'gg', 'hh', 'ee"
    return render(request, "exam/exam.html", {"ti": x})

def answerpage(request):
    return render(request, 'exam/answerpg.html')