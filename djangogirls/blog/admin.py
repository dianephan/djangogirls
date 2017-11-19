#create admin credentials for the website
from django.contrib import admin


# Register your models here.
from .models import Post

admin.site.register(Post)   #make model visible on the admin page
