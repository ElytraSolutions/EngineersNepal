from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime
from .views import PostCreate, PostUpdate, PostDelete, SignUpView, profile, categoryview, AdminView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('create-post/', PostCreate.as_view(), name='create-post'), 
    path('update-post/<slug:slug>', PostUpdate.as_view(), name='update-post'), 
    path('delete-post/<slug:slug>', PostDelete.as_view(), name='delete-post'), 
    path('delete-post/<slug:slug>', PostDelete.as_view(), name='delete-post'), 
    path('profile-update', profile, name='profile'), 
    path('category/<slug:slug>', categoryview, name='category'), 
    path('profile/<slug:slug>', AdminView, name='adminpage'), 
]
