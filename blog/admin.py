from django.contrib import admin
from .models import BlogField,PublishingUser

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title' , 'slug' , 'author' , 'created_on')
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(PublishingUser)
admin.site.register(BlogField , BlogAdmin )
