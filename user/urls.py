

from django.urls import path, include
from django.conf import settings
from django.contrib.auth.views import LogoutView
from . import views
from django.conf.urls.static import static
 
urlpatterns = [
        path('', views.index, name ='index'),
        path('login/', views.Login, name ='login'),
        path('losgin/', views.logout_view, name ='logout'),
        #path("logout/", LogoutView.as_view(), name="logout"),        
        #path('logout/', LogoutView.as_view(template_name ='login.html'), name ='logout'),
        #url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),        
        #path('user/', include('django.contrib.auth.urls')),
        path('register/', views.register, name ='register'),         
]