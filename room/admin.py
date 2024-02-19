from django.contrib import admin
from .models import (
    Room,
    RoomServices,
    RoomImages,
    RoomContent,
    RoomReview,
)


class RoomContentAdmin(admin.TabularInline):
    model = RoomContent
    extra = 1


@admin.register(RoomServices)
class RoomServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomContentAdmin]
    list_display = ('id', 'title',)
    list_display_links = ('title',)
    readonly_fields = ('slug', 'created_date',)
    filter_horizontal = ('services',)


@admin.register(RoomImages)
class RoomImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_image')
    list_display_links = ('get_image',)
    search_fields = ('room',)


@admin.register(RoomReview)
class RoomReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'message', 'created_date')
    list_display_links = ('author', 'message',)
    search_fields = ('author', 'room',)
    readonly_fields = ('created_date',)



