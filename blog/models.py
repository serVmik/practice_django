from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):

    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'

    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000, blank=True, null=True, help_text='')
    data_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

