from django.db import models
import time
from django.contrib.auth.models import User

class Artist(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    bio = models.TextField(max_length=500)
    verified_artist = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # Here is our new column
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# below Artist Model

class Art(models.Model):

    title = models.CharField(max_length=150)
    length = models.IntegerField(default=0)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="arts")

    def __str__(self):
        return self.title

    def get_length(self):
        return time.strftime("%-Y:%H", time.gmtime(self.length))

# Category model
class Category(models.Model):

    title = models.CharField(max_length=150)
    # this is many-to-many field, this will create our join table
    arts = models.ManyToManyField(Art)

    def __str__(self):
        return self.title

