from django.db import models

class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100, blank=True, default='')
    time_create = models.DateTimeField(auto_now_add=True)
    mov = models.ForeignKey('Movie', on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ['created']


class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField(blank=True)
