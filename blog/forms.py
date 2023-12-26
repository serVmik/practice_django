from django.forms import ModelForm

from blog.models import Post


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
