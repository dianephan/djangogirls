from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User') #you are the user key
    title = models.CharField(max_length=200) #title that is not over 200 characters
    text = models.TextField()   #the body of our blog posts
    created_date = models.DateTimeField(
            default=timezone.now)       #output of the date the post was created/published on
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):      #create a function that will publish blog post so draft first then publish online
        self.published_date = timezone.now()
        self.save()

    def __str__(self):  #states that every single post has a title
        return self.title
