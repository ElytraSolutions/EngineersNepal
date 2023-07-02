from django.contrib import admin
from .models import Post, Author, Category, advertisement, Vacancy, Videos, TenderDocuments, AppliedUsers
# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(advertisement)
admin.site.register(Vacancy)
admin.site.register(Videos)
admin.site.register(TenderDocuments)
admin.site.register(AppliedUsers)


