from django.views.generic import ListView

from discussions.models import Discussion


class DiscussionsListView(ListView):
    """A view for displaying a list of all users discussions."""

    model = Discussion
    template_name = 'discussions/list.html'
    extra_context = {
        'title': 'Список всех дискуссий',
    }
