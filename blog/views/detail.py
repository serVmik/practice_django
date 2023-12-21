from django.views.generic import DetailView

from blog.models import Post


class UserPostDetailView(DetailView):
    """Display detail user post."""

    model = Post
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        queryset = Post.objects.get(pk=self.kwargs.get('pk'))
        context = super().get_context_data(**kwargs)
        context['blog_detail'] = queryset
        return context
