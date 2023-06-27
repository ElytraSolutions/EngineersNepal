from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from django.conf import settings 
User=get_user_model()
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    middlename=models.CharField(max_length=40, null=True, blank=True, default='')
    profile_picture = models.ImageField(default='default.jpg', upload_to='profilepics')
    bio=models.TextField(max_length=300, blank=True, null=True)
    facebook_link=models.URLField(blank=True, null=True)
    twitter_link=models.URLField(blank=True, null=True)
    youtube_link=models.URLField(blank=True, null=True)
    slug=models.SlugField(null=False, blank=True, unique=True)
    def save(self, *args, **kwargs):
        super(Author, self).save()
        if not self.slug:
            self.slug=slugify(self.user.username)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
    
    @property
    def fullname(self):
        return self.firstname+" "+ self.lastname


class Category(models.Model):
    title = models.CharField(max_length=40)
    slug=models.SlugField(null=False, blank=True, unique=True)
    
    def save(self, *args, **kwargs):
        super(Category, self).save()
        if not self.slug:
            self.slug=slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Post(models.Model):
    CHOICES = (
        ('EN', 'English'),
        ('NP', 'Nepali'),
    )

    title = models.CharField(max_length=100)
    timestamp = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='post_thumbs')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = RichTextUploadingField(blank=True, null=True,config_name='default')
    language=models.CharField(max_length=40, choices=CHOICES)
    slug = models.SlugField(null=False, blank=True, unique=True)

    def save(self, *args, **kwargs):
        super(Post, self).save()
        if not self.slug:
            self.slug=slugify(self.title)
        return super().save(*args, **kwargs)
    
    # def get_absolute_url(self):
    #     return reverse("Post-detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title




class advertisement(models.Model):
    #title of the advertisement
    title = models.CharField(max_length=100)
    #description of the advertisement
    #gif or image field
    photo = models.ImageField(upload_to='post_ads')
    #link to the post
    link = models.URLField()
    #date of creation
    date_created = models.DateField(auto_now_add=True)
    #date of expiry
    date_expiry = models.DateField()
    #status of the advertisement
    status = models.BooleanField(default=True)

    def str(self):
        return self.title
