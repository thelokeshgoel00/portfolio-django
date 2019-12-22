from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def allBlogs(request):
    blog = Blog.objects
    return render(request, 'blog/allblogs.html',{'Blog':blog})
def detail(request, blog_id):
    detailBlog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'Blog':detailBlog})