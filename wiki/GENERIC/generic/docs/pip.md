## django.contrib.humanize  
(англ. - очеловечивание шаблонов)  
[linc](https://docs.djangoproject.com/en/4.2/ref/contrib/humanize/)  


## [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)
#### settings.py  
```cfgrlanguage
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
```
```
ALLOWED_HOSTS = [
    # ...
]
```
#### urls.py  
```
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
```cfgrlanguage
if settings.DEBUG:
    
    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include('debug_toolbar.urls')),
    ]
```

## [channels](https://channels.readthedocs.io/en/latest/installation.html#installation)  
#### settings.py
```cfgrlanguage
INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    ...
    "channels",
    ...
)
```
> **Note:**  
> added without adding "daphne" to INSTALLED_APPS.

```cfgrlanguage
ASGI_APPLICATION = "practice_django.routing.application"
```

```cfgrlanguage
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}
```

  
#### routing.py
add ```routing.py``` to ```practice_django/```


## [jupyter-notebook](https://jupyter.org/install#jupyter-notebook)
```cfgrlanguage
poetry add --group dev notebook==6.5.6
```
> **Note:**  
> add only notebook==6.5.6

Для интеграции ```notebook``` с ```Django``` необходимо установить ```django-extensions```   
To run the notebook:
```cfgrlanguage
jupyter notebook
```


## [django-extensions](https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#installing)
```cfgrlanguage
poetry add --group dev django-extensions
```
[Configuration](https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration)
```cfgrlanguage
INSTALLED_APPS = (
    ...
    'django_extensions',
    ...
)
```

