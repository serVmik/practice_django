from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils import timezone
from ckeditor.fields import RichTextField


class Post(models.Model):
    """Post model."""

    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'

    title = models.CharField(
        max_length=200,
        help_text='Не более 200 символов',
        # If True, a database index will be created for this field.
        # Если заголовок индексируется, то поиск осуществляется быстрее,
        # при наличии искомого слова в индексе.
        # https://docs.djangoproject.com/en/4.2/ref/models/fields/#db-index
        db_index=True
    )
    # content = models.TextField(max_length=2000, blank=True, null=True, help_text='')
    content = RichTextField(
        max_length=5000,
        blank=True,
        null=True,
        help_text='не более 5000 символов',
    )
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#slugfield
    slug = models.SlugField(
        max_length=50,
        # https://docs.djangoproject.com/en/4.2/ref/models/fields/#unique
        # при использовании в url slug обязательно
        # добавлять id + get_absolute_url()
        # unique=True,
    )
    likes = models.ManyToManyField(User, related_name='reply_ok', blank=True)
    reply = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='reply_ok',
        on_delete=models.CASCADE
    )

    # slugify

    def total_likes(self):
        """Return number of likes."""
        return self.likes.count()

    def get_absolute_url(self):
        """Override get_absolute_url."""
        return reverse_lazy('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
