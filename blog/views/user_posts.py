"""
Задача вывести посты пользователя.

Как мы будем выводить.
Представление смысл - какие методы QuerySet выборки нам выводить.
    написать менеджер
    a = Post.objects.filter(
    написать класс

    написать функцию
"""
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from blog.models import Post


class UserPostListView(ListView):
    """Display users posts list view."""

    model = Post
    template_name = 'blog/list.html'

    # именование переменной представление_модель_что-это
    # context_object_name = 'blog_post_user_list'
    #
    # def get_queryset(self):
    #     """Return posts user.
    #
    #     Get login user posts from Post model. Posts ordered by created date.
    #     Upper post is the last post.
    #     """
    #     # Не используем super(), так как идет обращение к конкретному
    #     # пользователю.
    #     # Получаем 'user' по полю 'username' модели 'User' со значением,
    #     # взятом из kwargs по ключу 'username'.
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Post.objects.filter(author=user).order_by('-data_created')

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        queryset = Post.objects.filter(author=user)
        context = super().get_context_data(**kwargs)
        context['object_list'] = queryset.order_by('-date_created')
        return context
