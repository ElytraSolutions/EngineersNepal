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


class ContactUSForm(forms.Form):
     email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control valid", "name": "email", "id": "email", "type": "email",
                                                           "onfocus": "this.placeholder = ''", "onblur": "this.placeholder = 'Enter email address'", "placeholder": "Email"}))
     subject = forms.CharField(max_length=254, widget=forms.TextInput(attrs={"class": "form-control", "name": "subject", "id": "subject",
                                                                            "type": "text", "onfocus": "this.placeholder = ''", "onblur": "this.placeholder = 'Enter Subject'", "placeholder": "Enter Subject"}))
     message_body = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control w-100", "name": "message", "id": "message", "cols": "30",
                                                        "rows": "9", "onfocus": "this.placeholder = ''", "onblur": "this.placeholder = 'Enter Message'", "placeholder": " Enter Message"}))
     name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control valid", "name": "name", "id": "name",
                                                                         "type": "text", "onfocus": "this.placeholder = ''", "onblur": "this.placeholder = 'Enter your name'", "placeholder": "Enter your name"}))

     def str(self):
        return self.Email
    
    