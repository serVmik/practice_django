from django.urls import path

from discussions import views

app_name = 'discussions'
urlpatterns = [
    path(
        'create/',
        views.discussions_create,
        name='create',
    ),
    path(
        'list/',
        views.DiscussionsListView.as_view(),
        name='all',
    ),
    path(
        'user/<str:username>/',
        views.UserDiscussionListView.as_view(),
        name='user'
    ),
    path(
        '<int:pk>/',
        views.DiscussionDetailView.as_view(),
        name='detail',
    ),
]
