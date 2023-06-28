from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from .models import Post, Author, Category
from .forms import ContactUSForm
from datetime import datetime
from .forms import PostForm, UserUpdateForm, ProfileUpdateForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    def get_success_url(self):
        slug=self.kwargs['slug']
        return reverse_lazy('newsdetail', kwargs={'slug':slug})

class PostDelete(DeleteView, LoginRequiredMixin, SuccessMessageMixin):
    model=Post
    success_url='/'
    success_message='post deleted successsfully'



class SignUpView(CreateView, SuccessMessageMixin):
    template_name='home/signup.html'
    success_url=reverse_lazy('login')
    form_class=UserRegisterForm
    success_message='Signed Up successfully'


@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.author)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'profile updates successfully')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.author)
    context={'u_form':u_form, 
                 'p_form':p_form, 
                 'user':request.user}
    return render(request, 'home/profile_update.html', context)


def categoryview(request, slug):
    searched=Post.objects.filter(categories__slug=slug).order_by('timestamp')
    categories=Category.objects.all()
    item=Category.objects.get(slug=slug)
    page=request.GET.get('page', 1)
    paginator=Paginator(searched, 4)
    try:
        a_post = paginator.page(page)
    except PageNotAnInteger:
        a_post = paginator.page(1)
    except EmptyPage:
        a_post = paginator.page(paginator.num_pages)
    context={'item':item, 
             'searched':searched, 
             'posts':a_post,
             'categories':categories,
             'cate':Category.objects.get(slug=slug),
             }
    return render(request, 'home/category.html',context)


def AdminView(request, slug):
    author=Author.objects.get(slug=slug)
    categories=Category.objects.all()
    searched=Post.objects.filter(author__slug=slug).order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(searched, 6)
    try:
        a_post = paginator.page(page)
    except PageNotAnInteger:
        a_post = paginator.page(1)
    except EmptyPage:
        a_post = paginator.page(paginator.num_pages)
    context={
        'posts':a_post,
        'author':author,
        'categories':categories,
    }
    return render(request, 'home/admin.html', context)


def searchview(request):
    if request.method == "POST":
        query = request.POST['search']
        if query:
            queryset=queryset.filter(
                Q(title__contains=query) | 
                Q(content__contains=query)).distinct()
        page=request.GET.get('page',1)
        paginator=Paginator(queryset, 6)
        try:
            a_post = paginator.page(page)
        except PageNotAnInteger:
            a_post = paginator.page(1)
        except EmptyPage:
            a_post = paginator.page(paginator.num_pages)
        context={
            'posts':a_post, 
            'query':query,
        }
        return render(request, 'home/searchresult.html', context)


def contact(request):
    Contactform = ContactUSForm(request.POST)
    if request.method == 'POST':
        if Contactform.is_valid():
            email = Contactform.cleaned_data['email']
            print(email)
            subject = Contactform.cleaned_data['subject']
            print(subject)
            message_body=Contactform.cleaned_data['message_body']
            print(message_body)
            name=Contactform.cleaned_data['name']
            print(name)
            
        else:
         Contactform = ContactUSForm(request.POST)    
            
    context={'form':Contactform}
    return render(request, 'home/contact.html', context)

def aboutus(request):
    context={}
    return render(request, 'home/about.html', context)


def homepage(request):
    category_dict={}
    all_posts=Post.objects.all()
    featured_post=Post.objects.filter(featured=True).order_by('-timestamp')[0]
    trending_1=all_posts[:3]
    trending_2=all_posts[3:8]
    categories=Category.objects.all()

    for category in categories:
        if category.featured==True:
            category_dict[category]=Post.objects.filter(categories__slug=category.slug).order_by('-id')[:7]
    # finding weekly top posts
    # print(category_dict) 
    weekly_top=Post.objects.filter(timestamp__week=datetime.now().date().isocalendar()[1]).order_by('-id')[:7]
    context={'trending1':trending_1,'trending2':trending_2, 'featured_post':featured_post, 'weekly_top':weekly_top,
             'categories':categories, 'category_dict':category_dict}
    return render(request,'home/home.html',context)

def newsdetail(request,slug):
    context={'news':Post.objects.get(slug=slug),}
    return render(request,'home/newsdetail.html',context)
    
