from django.db import models
from datetime import datetime

#Blog model Class
#Date: 2021-11-14
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    publish_date = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title 

#Comment model Class
#Date: 2021-11-15
class Comment(models.Model):
    postIdMap = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateField(default=datetime.now)

    def __str__(self):
        return self.author
