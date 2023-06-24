from django import forms 
from .models import Post, Author
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ['title','thumbnail','categories','content','language']
        widgets = {
            'category': forms.Select(),
            'body': forms.Textarea(),
            'content': forms.TextInput(),
            'language':forms.Select(),
        }

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Author
        fields = ['profile_picture', 'bio','twitter_link','facebook_link','youtube_link']

