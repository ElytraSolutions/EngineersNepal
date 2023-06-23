from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from .models import Post, Author
from datetime import datetime
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class PostCreate(CreateView, LoginRequiredMixin):
    model=Post
    form_class=PostForm
    queryset=Post.objects.all()
    def form_valid(self, form):
        form.instance.timestamp = datetime.now().date()
        author=Author.objects.get(user=self.request.user)
        form.instance.author=author
        form.save()
        messages.success(self.request, f'created post successfully')
        return super(PostCreate, self).form_valid(form)
    
class PostUpdate(UpdateView, LoginRequiredMixin, SuccessMessageMixin):
    model=Post
    form_class=PostForm
    queryset=Post.objects.all()
    success_message="post updated successfully"

class PostDelete(DeleteView, LoginRequiredMixin, SuccessMessageMixin):
    model=Post
    success_url='/home/'
    success_message='post deleted successsfully'

class PostDetail(DetailView):
    model=Post

    