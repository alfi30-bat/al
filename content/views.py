import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
import os
# Create your views here.

from user.models import use_info
from django.contrib.auth import get_user




def mainn(request):
    return render(request, 'content/main.html' )

@csrf_exempt

def load(request):
    global file_count
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            global nam
            nam = data.get('nam')
            # Process the data as needed
            response_data = {'status': 'success', 'aim_received': nam}
            print(nam)
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)    
    #nam="heat"    
    df=pd.read_excel("sample.xlsx")
    try:
        df_cleaned = df.dropna()
        conte= df_cleaned[nam].tolist()  
        print(len(conte))
        
    except KeyError:
        return render(request, 'content/main.html' )
    except NameError:
        return render(request, 'content/main.html' )    
    user = get_user(request)
    username = user.username
    if username=="":    
        print(username) 
        cat="null"
        cla="null"
        return render(request, 'content/page.html', {'max':json.dumps(conte), 'cate':cat, 'cla':cla } )
    else:
        blog = use_info.objects.get(username=username)
        cat= blog.category
        cla= blog.classs               
        scor= blog.score      
        print(scor)         
        return render(request, 'content/page.html', {'max':json.dumps(conte), 'cate':cat, 'cla':cla, 'score':scor } )
