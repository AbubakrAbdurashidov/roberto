from django.shortcuts import render
from .models import (
    Blog
)


def blog_list(request):
    ctx = {

    }
    return render(request, 'blog/blog.html', ctx)


def blog_detail(request, slug):
    blogs = Blog.objects.all(Blog, slug=slug)
    ctx = {
        'blogs': blogs
    }
    return render(request, 'blog/single-blog.html', ctx)