from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from discussions.forms import DiscussionCreateForm


# The login_required decorator
# https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-login-required-decorator
@login_required
def discussions_create(request):
    """Create discussion"""
    # Если запрос Post, тогда обрабатываем форму.
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.method
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.POST
    if request.method == 'POST':
        # Создадим экземпляр формы
        # и заполним его данными запроса (укажем параметры)
        # Получим данные POST для заполнения формы.
        request_form_data = request.POST
        # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.POST
        request_files = request.FILES
        # Создадим форму для редактирования.
        form = DiscussionCreateForm(request_form_data, request_files)

        if form.is_valid:
            new_discussion = form.save(commit=False)
            # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.user
            new_discussion.author = request.user

            new_discussion.save()
            messages.success(request, 'Дискуссия добавлена')
            # Редирект по get_absolute_url
            # модели Discussion формы DiscussionCreateForm
            return redirect(new_discussion.get_absolute_url())

    else:
        # Если поступит GET запрос или другой, вернуть пустую форму
        form = DiscussionCreateForm()

    return render(request, 'discussions/create_form.html', {'form': form})
