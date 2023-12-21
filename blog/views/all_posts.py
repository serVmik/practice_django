from django.views.generic import ListView

from blog.models import Post


class PostListView(ListView):
    """Display posts all users."""

    model = Post
    template_name = 'blog/list.html'
