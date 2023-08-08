from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from django.core.validators import FileExtensionValidator
from django.conf import settings 
from PIL import Image
User=get_user_model()
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    middlename=models.CharField(max_length=40, null=True, blank=True, default='')
    profile_picture = models.ImageField(upload_to='profilepics', default='default.png')
    bio=models.TextField(max_length=300, blank=True, null=True)
    facebook_link=models.URLField(blank=True, null=True)
    twitter_link=models.URLField(blank=True, null=True)
    youtube_link=models.URLField(blank=True, null=True)
    slug=models.SlugField(null=False, blank=True, unique=True)
    def save(self, *args, **kwargs):
        super(Author, self)
        if not self.slug:
            self.slug='2000'+str(self.user.username)
        # img=Image.open(self.profile_picture.path)
        # output_size=(350,350)
        # img.thumbnail(output_size)
        # img.save(self.profile_picture.path)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
    
    @property
    def fullname(self):
        return self.firstname+" "+ self.lastname
    
class advertisement(models.Model):
    #title of the advertisement
    title = models.CharField(max_length=100)
    hits=models.IntegerField(default=1)
    #gif or image field
    photo = models.ImageField(upload_to='post_ads')
    #link to the post
    link = models.URLField()
    #date of creation
    date_created = models.DateField(auto_now_add=True)
   
    #status of the advertisement
    status = models.BooleanField(default=True)
    original_photo=None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_photo=self.photo
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.photo != self.__original_photo:
            self.hits=1
        super().save(force_insert, force_update, *args, **kwargs)
        self.__original_photo=self.photo
        
    def __str__(self):
        return self.title
    



class Category(models.Model):
    choices=(
        ('gridone','gridone'),
        ('gridtwo','gridtwo'),
    )
    title = models.CharField(max_length=40)
    slug=models.SlugField(null=False, blank=True, unique=True)
    featured=models.BooleanField(default=False)
    priority=models.IntegerField(default=99)
    grid=models.CharField(max_length=10, choices=choices)

    #advertisement that can be included in the category, which can be null also
    desktop_ad=models.ForeignKey(advertisement, on_delete=models.SET_NULL, null=True,blank=True, related_name='destop_ad')
    mobile_ad=models.ForeignKey(advertisement, on_delete=models.SET_NULL, null=True,blank=True, related_name='mobile_ad')
    def save(self, *args, **kwargs):
        super(Category, self).save()
        if not self.slug:
            self.slug=slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    timestamp = models.DateField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='post_thumbs', default='post_thumbs/default.jpg')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = RichTextUploadingField(blank=True, null=True,config_name='default')
    slug = models.SlugField(null=False, blank=True, unique=True, allow_unicode=True)
    featured=models.BooleanField(default=False)
    views=models.IntegerField(default=1)
    approved=models.BooleanField(default=False)
    breaking=models.BooleanField(default=False)
    breakingthumbnail=models.BooleanField(default=True)

    

    def save(self, *args, **kwargs):
        super(Post, self).save()
        if not self.slug:
            formatedDate=datetime.now().strftime("%Y-%m-%d")
            self.slug=slugify(formatedDate)+'-'+'2000'+str(self.id)
        if not self.timestamp:
            self.timestamp=datetime.now()
        # img=Image.open(self.thumbnail.path)
        # output_size=(750,335)
        # img.thumbnail(output_size)
        # img.save(self.thumbnail.path)
        return super().save(*args, **kwargs)
    
    # def get_absolute_url(self):
    #     return reverse("Post-detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title






# model for vacany posts 
class Vacancy(models.Model):
    choices=(
        ('Onsite','Onsite'),
        ('Remote','Remote'),
    )
    title=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    description=RichTextUploadingField(blank=True, null=True,config_name='default')
    date_created=models.DateField(auto_now_add=True)
    date_expiry=models.DateField()
    address=models.CharField(max_length=100)
    place=models.CharField(max_length=10, choices=choices)
    worktime=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)
    link=models.URLField(null=True, blank=True, default='')
    def __str__(self):
        return self.title

class Videos(models.Model):
    title=models.CharField(max_length=100)
    link=models.URLField()
    date_created=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    

class TenderDocuments(models.Model):
    title=models.CharField(max_length=400)
    documents=models.FileField(upload_to='tender_documents')
    date_created=models.DateField(auto_now_add=True)
    date_exp=models.DateField()
    def __str__(self):
        return self.title

# model to store the applied users data 
class AppliedUsers(models.Model):
    vacancy=models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    # only upload files with extensions pdf 
    cv=models.FileField(upload_to='cv')
    def __str__(self):
        return self.fullname+" "+self.vacancy.title
    

class Epapers(models.Model):
    epaper_pdf=models.FileField(upload_to='epapers', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    date_created=models.DateField()
    def __str__(self):
        return str(self.date_created)+" epaper"
    

class Comments(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    comment=models.TextField()
    date=models.DateField(auto_now_add=True)
    verified=models.BooleanField(default=False)
    def __str__(self):
        return self.name+" "+self.post.title

