from django import forms 
from .models import Post
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
