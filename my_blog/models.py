from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.html import strip_tags
import markdown

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
    #阅读量  0或正整数
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('my_blog:detail',args=[self.id])

    def increase_views(self):
        self.views +=1
        self.save(update_fields=['views'])

    def save(self,*args,**kwargs):
        #如果摘要不存在
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_time']
    

    
