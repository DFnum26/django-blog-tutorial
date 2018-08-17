from django.shortcuts import render
from .models import Post,Category
import markdown
from comments.forms import CommentForm
# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request,'my_blog/index.html',context={'post_list':post_list})

def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    )
    return render(request,'my_blog/index.html',context={'post_list':post_list})

def categories(request, category_id):
    post_list = Post.objects.filter(category=category_id
                                    )
    return render(request,'my_blog/index.html',context={'post_list':post_list})

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post':post, 'form':form, 'comment_list':comment_list}
    return render(request, 'my_blog/detail.html', context)
