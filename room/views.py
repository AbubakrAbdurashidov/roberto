from django.shortcuts import render


def room_list(request):
    ctx = {

    }
    return render(request, 'room/room.html', ctx)


def room_detail(request):
    ctx = {

    }
    return render(request, 'room/single-room.html')
