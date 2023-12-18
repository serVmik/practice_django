from django.contrib import admin
from blog.models import Post

# var1
# admin.site.register(Post)

@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title',]
