from django.contrib import admin
from .models import Artist, Art, Playlist

# Register your models here.
admin.site.register(Artist)
admin.site.register(Art)
admin.site.register(Playlist)