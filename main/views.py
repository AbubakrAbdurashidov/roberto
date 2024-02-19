from django.shortcuts import render


def home_view(request):
    ctx = {

    }
    return render(request, 'main/index.html', ctx)


def about_view(request):
    ctx = {

    }
    return render(request, 'main/about.html', ctx)


def contact_view(request):
    ctx = {

    }
    return render(request, 'main/contact.html', ctx)