from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    list_display = ['title', 'date_created', 'date_updated', 'author']
    prepopulated_fields = {'slug': ('title',)}
