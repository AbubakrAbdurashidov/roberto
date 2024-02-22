from django.shortcuts import render
from django.core.paginator import Paginator
from room.models import (
    Room,
    RoomImages,
    RoomServices
)


def room_list(request):
    rooms = Room.objects.all()
    services = RoomServices.objects.all()
    images = RoomImages.objects.all()
    paginator = Paginator(rooms, 1)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    ctx = {
        'page_obj': page_obj,
        'services': services,
        'images': images
    }
    return render(request, 'room/room.html', ctx)


def room_detail(request):
    ctx = {

    }
    return render(request, 'room/single-room.html')
