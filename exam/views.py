from django.contrib.auth import get_user
from django.shortcuts import render, get_object_or_404
import sqlite3, random,json
from random import randint
from django.core.exceptions import ObjectDoesNotExist

from .models import phy_easy
from user.models import use_info


from django.db.models import Count
# Create your views here.
def exampage(request):
    print(request)
    subject = request.POST.get('subject')
    if subject==None:
        print("nione")
    print(5, subject)
    i=1
    # Iterate through the dictionary and add each item to the array
    #row = phy_easy.objects.get(id=1)
    count = phy_easy.objects.aggregate(count=Count('id'))['count']
    random_index = randint(0, count - 1)
    print(phy_easy.objects.all()[random_index])
    x=[]
    global dans
    dans=[]
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
        if row.danswer==None:
            dans.append(row.danswer_img)
        else:
            dans.append(row.danswer)
        i=i+1    
    print(x)
    x=str(x)
    x=x.replace("['", "")
    x=x.replace("']", "")
    #x="jeson', 'e', 'f', 'g', 'h', 'e', 'alfred', 'a', 'b', 'c', 'd', 'd', 'alfredoooo', 'aa', 'ba', 'cc', 'dd', 'cc', 'jesonnnnnn', 'e', 'ff', 'gg', 'hh', 'ee"
    return render(request, "exam/exam.html", {"ti": x, 'dans':json.dumps(dans)})

def answerpage(request):
    if request.method == 'POST':
        print(request)
        data = json.loads(request.body)
        item1 = data.get('item1')
        print(item1)     
        user = get_user(request)
        username = user.username    
        print(username)    
        blog = use_info.objects.get(username=username)     
        print(blog)
        blog.score=int(blog.score)+int(item1)  
        blog.save()
        blog = use_info.objects.get(username=username)  
        h=blog.score
        print(h)   
    return render(request, 'exam/answerpg.html', {'score':'h'})


def danswerpage(request):
    try:
        user = get_user(request)
        username = user.username            
        blog = use_info.objects.get(username=username)     
        print(blog)        
        return render(request, 'exam/detailans.html', {'dans':json.dumps(dans), 'score':blog.score} )
    except use_info.DoesNotExist:
        print("advertisment")
        return render(request, 'exam/detailans.html', {'dans':json.dumps(dans), 'lo': "please login to save your score"})