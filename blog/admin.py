from django.contrib import admin
from .models import BlogField,PublishingUser,BlogComment

@admin.register(BlogField)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title' , 'slug' , 'author' , 'created_on')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(BlogComment)
class BlogComment(admin.ModelAdmin):
    list_display = ('CommentPost' , 'author' , 'content' , 'date_posted')
    search_fields = ('author' , 'comment')


# Register your models here.
admin.site.register(PublishingUser)

