from django.urls import path
from .views import (
    blog_list,
    blog_detail
)

app_name = 'blog'

urlpatterns = [
    path('list/', blog_list, name='list'),
    path('detail/', blog_detail, name='detail')
]