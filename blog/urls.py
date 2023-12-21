from django.urls import path

from blog import views

app_name = 'posts'
urlpatterns = [
    path(
        'create/',
        views.CreatePost.as_view(),
        name='create',
    ),
    path(
        'list/',
        views.PostListView.as_view(),
        name='all',
    ),
    path(
        'user/<str:username>/',
        views.UserPostListView.as_view(),
        name='user',
    ),
    path(
        '<int:pk>/',
        views.UserPostDetailView.as_view(),
        name='detail',
    ),
]
