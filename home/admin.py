from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','categories','breaking']
    search_fields = ['title']
    list_filter = ['categories','breaking']


 



# Register your models here.

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(advertisement)
admin.site.register(Vacancy)
admin.site.register(Videos)
admin.site.register(TenderDocuments)
admin.site.register(AppliedUsers)
admin.site.register(Epapers)






   