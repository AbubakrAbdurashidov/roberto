from django.shortcuts import render


def blog_list(request):
    ctx = {

    }
    return render(request, 'blog/blog.html', ctx)


def blog_detail(request):
    ctx = {

    }
    return render(request, 'blog/single-blog.html', ctx)