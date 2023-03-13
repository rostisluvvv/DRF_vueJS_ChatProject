from django.contrib import admin

from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ('creator', 'invited_user', 'date')


    def invited_user(self, obj):
        return '\n'.join([user.username for user in obj.invited.all()])


admin.site.register(Room, RoomAdmin)
