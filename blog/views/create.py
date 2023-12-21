from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from blog.forms import CreatePostForm


class CreatePost(LoginRequiredMixin, CreateView):
    """Create post view."""

    form_class = CreatePostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        """
        Add current user on author field Task model.
        Override success_url.
        """
        form.instance.author = self.request.user
        self.success_url = reverse_lazy(
            'posts:user',
            kwargs={'username': self.request.user.username}
        )
        return super().form_valid(form)
