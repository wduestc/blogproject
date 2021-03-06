# coding:utf-8
import markdown
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Post
from .models import Category
from comments.forms import CommentForm
# Create your views here.
def index(request):
    """
    return render(request, 'blog/index.html', context={
        'title':'我的博客首页',
        'welcome':'欢迎访问我的博客首页'
    })
    """
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})
    #return HttpResponse("欢迎访问我的博客首页")

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                 extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                 ])
    #记得在顶部导入commentform
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post':post,
               'form':form,
               'comment_list':comment_list
               }
    return render(request, 'blog/detail.html', context=context)

def archives(request, year, month):
    post_list = Post.objects.all().filter(created_time__year=year,
                                          created_time__month=month
                                          ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})