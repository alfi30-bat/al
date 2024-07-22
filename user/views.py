from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .models import use_info
from django.http import JsonResponse
import json

#################### index####################################### 
def index(request):
	return render(request, 'user/index.html', {'title':'index'})

########### register here ##################################### 
def register(request):
	print("register")
	if request.method == 'POST':
		print("t")
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			print("q", request.body)
			print("q", request.POST)
			form.save()
			username = request.POST.get('username')
			email = request.POST.get('email')
			classs = request.POST.get('classs')
			category = request.POST.get('category')
			######################### mail system #################################### 
			#htmly = get_template('user/Email.html')
			#d = { 'username': username }
			#subject, from_email, to = 'welcome', 'alfredjesonaj@gmail.com', email
			#html_content = htmly.render(d)
			#msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			#msg.attach_alternative(html_content, "text/html")
			#msg.send()
			################################################################## 
			use_info.objects.create(username=username, email= email, classs=classs, category= category, score=0)
			messages.success(request, f'Your account has been created ! You are now able to log in')
			return redirect('login')
	else:
		print("herer")
		form = UserRegisterForm()
	return render(request, 'user/register.html', {'form': form, 'title':'register here'})

################ login forms################################################### 
def Login(request):
	if request.method == 'POST':

		# AuthenticationForm_can_also_be_used__

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' welcome {username} !!')
			return redirect('index')
		else:
			messages.info(request, f'account done not exit plz sign in')
	form = AuthenticationForm()
	return render(request, 'user/login.html', {'form':form, 'title':'log in'})
