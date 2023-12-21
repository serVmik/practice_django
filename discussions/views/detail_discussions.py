from django.views.generic import DetailView

from discussions.models import Discussion


class DiscussionDetailView(DetailView):
    model = Discussion
    template_name = 'discussions/detail.html'
    context_object_name = 'discussion_detail'
