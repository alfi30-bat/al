import sqlite3
from django.http import HttpResponse
import random

from django.shortcuts import render
def button(request):
    return render(request, 'page.html')

def exampage(request):
    conn = sqlite3.connect('questions database.db')
    curosr = conn.cursor()
    curosr.execute("SELECT * FROM time_q")
    x=curosr.fetchall()
    print(x)
    questno=[1,2]
    questno=random.choice(questno)
    curosr.execute("SELECT * FROM time_q WHERE id= '{}'".format(questno))
    x=curosr.fetchone()
    x=str(x)
    questno=str(questno)
    x=x.replace("("+ questno +", '", "")
    x=x.replace("')", "")
    print(x)
    x="jeson', 'e', 'f', 'g', 'h', 'e', 'alfred', 'a', 'b', 'c', 'd', 'd', 'alfredoooo', 'aa', 'ba', 'cc', 'dd', 'cc', 'jesonnnnnn', 'e', 'ff', 'gg', 'hh', 'ee"
    return render(request, 'exam.html',  {'ti': x})

def answerpage(request):
    return render(request, 'answerpg.html')


conn = sqlite3.connect('questions database.db')
curosr = conn.cursor()
curosr.execute("SELECT * FROM time_q")
x=curosr.fetchall()
print(x)
questno=[1,2]
questno=random.choice(questno)
curosr.execute("SELECT * FROM time_q WHERE id= '{}'".format(questno))
x=curosr.fetchone()
x=str(x)
questno=str(questno)
x=x.replace("("+ questno +", '", "")
x=x.replace("')", "")
print(x)
y="(2, 'jeson', 'e', 'f', 'g', 'h', 'e')"
dicta={
    "1":x,
}
conn.commit()
conn.close()