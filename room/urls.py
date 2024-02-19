from django.urls import path
from .views import (
    room_list,
    room_detail
)

app_name = 'room'

urlpatterns = [
    path('list/', room_list, name='list'),
    path('detail/', room_detail, name='detail')
]