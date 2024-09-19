
from django.contrib import admin
from .models import PostProjects

@admin.register(PostProjects)
class PostProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image') 
    search_fields = ('title', 'description')  
    list_filter = ('title',)  
