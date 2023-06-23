from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime
from .views import PostCreate, PostUpdate, PostDelete


urlpatterns = [
    path('login/', LoginView.as_view(template_name='Login/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create-post/', PostCreate.as_view(), name='create-post'), 
    path('update-post/<slug:slug>', PostUpdate.as_view(), name='update-post'), 
    path('delete-post/<slug:slug>', PostDelete.as_view(), name='delete-post'), 
]
