from django.shortcuts import render
from room.models import (
    Room,
    RoomImages
)


def home_view(request):
    rooms = Room.objects.all()
    images = RoomImages.objects.all()
    ctx = {
        'images': images,
        'rooms': rooms
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