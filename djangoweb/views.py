import sqlite3
from django.http import HttpResponse
import random
import os

from django.shortcuts import render
global file_count
file_count=7
def button(request):
    global file_count
  
    folder_path = './static/heat'
    file_count = len([name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name))])
    print(f'The number of files in {folder_path} is {file_count}')


    return render(request, 'page.html', {'max':file_count} )

def logn(request):
    print("pattiiiiiiiiiiiiii")
    return render(request, 'login.html')

def signin(request):
    g= request.GET
    print(g)
    u= dict(g.lists())
    print(u)
    mail = g['email']
    usename = g['username']
    year = g['number']
    passw = g['pass']
    conn = sqlite3.connect('user.db')
    curosr = conn.cursor()
    curosr.execute("create table if not exists users (email text, username,  yearofexam, password)")
    curosr.execute("SELECT email ,username FROM users WHERE email=? OR username=?",
                (mail, usename))

    # Fetch one result from the query because it
    # doesn't matter how many records are returned.
    # If it returns just one result, then you know
    # that a record already exists in the table.
    # If no results are pulled from the query, then
    # fetchone will return None.
    result = curosr.fetchone()

    if result:
            
        conn.commit()
        conn.close()    
        return render(request, 'login.html', {'info':"username or email already exists"})
        # Record already exists
        # Do something that tells the user that email/user handle already exists
    else:
        curosr.execute("insert into users (email, username, yearofexam, password) values (?, ?, ?, ?)",
        (mail, usename, year, passw))
        sc=0
        curosr.execute("create table if not exists scores (username, score)")
        curosr.execute("insert into scores (username, score) values (?, ?)",
        (usename, sc))
        conn.commit()
        conn.close() 
        global file_count

        return render(request, 'page.html', {'max':file_count, 'name':usename} )
        

def login(request):
    global file_count
    conn = sqlite3.connect('user.db')
    curosr = conn.cursor()    
    g=request.GET
    email=g['email']
    passw=g['pass']
    curosr.execute("SELECT password,username FROM users WHERE email= '{}'".format(email))
    x=curosr.fetchone()
    print(x)
    conn.commit()
    conn.close()           
    if x==None:
      print("wrong")  
      return render(request, 'login.html', {'info':"wrong ID or password"})

    elif x[0]==passw :
        print("correct")
        return render(request, 'page.html', {"name":x[1], 'max':file_count})
    else:
        print("wrong")  
        return render(request, 'login.html', {'info':"wrong ID or password"})

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
    conn.commit()
    conn.close()    
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