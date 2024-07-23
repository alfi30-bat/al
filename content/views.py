from django.shortcuts import render
import os
# Create your views here.
from user.models import use_info
from django.contrib.auth import get_user

global file_count
file_count=7

def load(request):
    global file_count
    user = get_user(request)
    username = user.username
    if username=="": 
        folder_path = 'content/static/content/heat'
        file_count = len([name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name))])
        print(f'The number of files in {folder_path} is {file_count}')        
        print(username) 
        cat="null"
        cla="null"
        return render(request, 'content/page.html', {'max':file_count, 'cate':cat, 'cla':cla } )
    else:
        folder_path = 'content/static/content/heat'
        file_count = len([name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name))])
        print(f'The number of files in {folder_path} is {file_count}')
        blog = use_info.objects.get(username=username)
        cat= blog.category
        cla= blog.classs
        return render(request, 'content/page.html', {'max':file_count, 'cate':cat, 'cla':cla } )
