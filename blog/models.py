# coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    标签类
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    """
    文章标题
    """
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    #文章摘要 blank=True 参数值允许为空 null=true
    excerpt = models.CharField(max_length=200, blank=True)

    #如果是存在一对多的关系 则需要使用到外键
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    #Users是通过django.contrib.auth.models 导入的
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})


