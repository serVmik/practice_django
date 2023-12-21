from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from pytils.translit import slugify
# from slugify import slugify
from django.urls import reverse


class Discussion(models.Model):
    class Meta:
        verbose_name = 'Дискуссия'
        verbose_name_plural = 'Дискуссии'

    title = models.CharField(
        max_length=200,
        help_text='Не более 200 символов',
        db_index=True,
    )
    content = RichTextField(
        max_length=5000,
        help_text='Не более 5000 символов',
        blank=True,
        null=True,
    )
    date_created = models.DateTimeField(
        default=timezone.now,
    )
    date_updated = models.DateTimeField(
        auto_now=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(
        max_length=50,
        # unique=True - подумать
    )
    likes_discussions = models.ManyToManyField(
        User,
        related_name='discussion_likes',
        blank=True,
        verbose_name='Сохраненные посты',
    )
    save_discussion = models.ManyToManyField(
        User,
        related_name='blog_discussion_save',
        blank=True,
        verbose_name='Сохраненные посты',
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Discussion, self).save(*args, **kwargs)

    def total_likes_discussions(self):
        return self.likes_discussions.count()

    def total_saves_discussions(selfs):
        return selfs.save_discussion.count()

    def get_absolute_url(self):
        return reverse('discussions:user', kwargs={'pk': self.pk})

    # методы модели
