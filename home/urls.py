from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime
from .views import (PostCreate, PostUpdate, PostDelete, SignUpView, profile,
categoryview, AdminView, searchview,contact, aboutus,newsdetail, homepage, vacancyhome, vacancy, tender, apply, epaperview, videos, downloadcsv)
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',homepage,name='home'),
    path('posts/<slug:slug>/',newsdetail,name='newsdetail'),
    path('login/', LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('create-post/', PostCreate.as_view(), name='create-post'), 
    path('update-post/<slug:slug>', PostUpdate.as_view(template_name='home/post_update_form.html'), name='update-post'), 
    path('delete-post/<slug:slug>', PostDelete.as_view(), name='delete-post'), 
    path('delete-post/<slug:slug>', PostDelete.as_view(), name='delete-post'), 
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='register/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='register/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='register/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='register/password_reset_complete.html'), name='password_reset_complete'),
    path('profile-update/', profile, name='profile'), 
    path('search/', searchview, name='search'), 
    path('vacancy/', vacancyhome, name='vacancyhome'), 
    path('vacancy/<int:id>/', vacancy, name='vacancy'), 
    path('contact/', contact, name='contact'), 
    path('about-us/', aboutus, name='aboutus'), 
    path('tenders/', tender, name='tenders'), 
    path('category/<slug:slug>', categoryview, name='category'), 
    path('author/<slug:slug>', AdminView, name='adminpage'), 
    path('apply/<int:id>', apply, name='apply'), 
    path('epaper/<int:id>/', epaperview, name='epaper'), 
    path('videos/', videos, name='videos'), 
    path('download/<int:id>/', downloadcsv, name='download')
]
