from django.contrib import admin
from .models import Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    class meta:
        model = Post
    list_display = ['title', 'content','timestamp','updated']
    list_display_links = ['timestamp']
    list_filter = ['title','content']
    search_fields = ['content']




admin.site.register(Post , PostModelAdmin)