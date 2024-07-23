

from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth
from . import views
from django.conf.urls.static import static
 
urlpatterns = [
        path('', views.index, name ='index'),
        path('login/', views.Login, name ='login'),
        path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),
        #path('user/', include('django.contrib.auth.urls')),
        path('register/', views.register, name ='register'),         
]