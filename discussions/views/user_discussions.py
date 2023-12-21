from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from discussions.models import Discussion


class UserDiscussionListView(ListView):
    """Display a list of user discussions"""

    model = Discussion
    template_name = 'discussions/list.html'

    def get_context_data(self, **kwargs):
        user = get_object_or_404(
            User,
            username=self.kwargs.get('username'),
        )
        queryset = Discussion.objects.filter(author=user)
        context = super().get_context_data(**kwargs)
        context['object_list'] = queryset.order_by(
            '-date_created'
        )
        context['title'] = 'Список моих дискуссий'
        return context
