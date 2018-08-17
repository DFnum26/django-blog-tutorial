from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Tag(models.Model):
    '''标签'''
    text = models.CharField(max_length=75)

    def __str__(self):
        return self.text
    

class Category(models.Model):
    '''类别'''
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text
    

class Post(models.Model):
    '''文章'''
    title = models.CharField(max_length=75)

    body = models.TextField()

    created_time = models.DateTimeField()
    
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200,blank=True)
    #类别一多
    category = models.ForeignKey(Category)
    #标签多对多
    tag = models.ManyToManyField(Tag)

    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('my_blog:detail',args=[self.id])

    class Meta:
        ordering = ['-created_time']
    

    
