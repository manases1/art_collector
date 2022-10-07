from unicodedata import category
from django.contrib import admin
from .models import Artist, Art, Category

# Register your models here.
admin.site.register(Artist)
admin.site.register(Art)
admin.site.register(category)