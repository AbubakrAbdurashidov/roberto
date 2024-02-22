from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.utils import timezone


class RoomServices(models.Model):
    images = models.ImageField(null=True, blank=True, upload_to='media/room_services')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


# class BookRoom(models.Model):
    # check_in = models.DateTimeField(default=timezone.now)
    # check_out = models.DateTimeField(default=timezone.now)
    # pass


class Room(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(editable=False, null=True, blank=True)
    price = models.DecimalField(max_digits=550, decimal_places=5)
    size = models.PositiveSmallIntegerField(default=1)
    capacity = models.PositiveSmallIntegerField(default=1)
    bed = models.CharField(max_length=255)
    services = models.ManyToManyField(RoomServices)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class RoomImages(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True, related_name='images')
    image = models.ImageField(null=True, blank=True, upload_to='media/room_image')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.room.title

    def get_image(self):
        if self.image:
            return mark_safe(
                f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="50" height="50" /></a>')
        return '-'


class RoomReview(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='review_room', null=True, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='room_review_autor')
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class RoomContent(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='content_room')
    content = RichTextField()
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.room.title


def room_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title + "-")


pre_save.connect(room_pre_save, sender=Room)





