# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from practice_django import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',
        TemplateView.as_view(template_name='templates_projects/home.html'),
        name='home'),
    path('posts/', include('blog.urls')),
    path('discussions/', include('discussions.urls')),

    # https://docs.allauth.org/en/latest/installation/quickstart.html#quickstart
    # path('accounts/', include('allauth.urls')),
    # End allauth
    # path(
    #     'users/',
    #     views.UserLoginView.as_view(),
    #     name='login'
    # ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# django-debug-toolbar
if settings.DEBUG:

    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include('debug_toolbar.urls')),
    ] + urlpatterns
# End django-debug-toolbar
