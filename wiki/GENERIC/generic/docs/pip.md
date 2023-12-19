## Create venv
### [poetry](https://python-poetry.org/)
```cfgrlanguage
sudo apt update
```
```cfgrlanguage
sudo apt install curl
```
Install a specific version:
```cfgrlanguage
curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.5.1 python3 -
```
Сheck installation success
```cfgrlanguage
poetry --version
```
#### Add Poetry to your PATH:
```cfgrlanguage
export PATH="/home/{user}/.local/bin:$PATH"
```
Enable the creation of a virtual environment:
```cfgrlanguage
poetry config virtualenvs.in-project true
```
Create the application directory:
```cfgrlanguage
mkdir practice_django  
cd practice_django
```
```cfgrlanguage
poetry install
```
[Create a virtual environment:](https://python-poetry.org/docs/cli#shell)
```cfgrlanguage
poetry shell
```
`Poetry` will create `.venv` in the current directory.



## **[mkdocs](https://www.mkdocs.org/)**
```cfgrlanguage
poetry add --group doc mkdocs
```
### [mkdocs-material](https://squidfunk.github.io/mkdocs-material/getting-started/#installation)
```cfgrlanguage
poetry add --group doc mkdocs-material
```
### [mkdocs-awesome-pages-plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin#installation)
```cfgrlanguage
poetry add --group doc mkdocs-awesome-pages-plugin
```




## [Django](https://www.djangoproject.com/download/)
```cfgrlanguage
poetry add django==4.2.8
```



## [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html#installation)
```cfgrlanguage
poetry add django-crispy-forms
```



## [django-cleanup](https://github.com/un1t/django-cleanup)
```cfgrlanguage
poetry add django-cleanup
```



## pillow
```cfgrlanguage
poetry add pillow
```



## [django-ckeditor](https://pypi.org/project/django-ckeditor/#installation)
```cfgrlanguage
django-ckeditor
```



## [django-allauth](https://docs.allauth.org/en/latest/installation/quickstart.html#quickstart)
Authorization library
```cfgrlanguage
poetry add django-allauth
```



## [python-dotenv](https://pypi.org/project/python-dotenv/)
```cfgrlanguage
poetry add python-dotenv
```
Create a file `.env` in the directory where the project is located (`BASE_DIR`).  
`.env`  
```cfgrlanguage
SECRET_KEY=...
```
`settings.py`
```cfgrlanguage
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
```



## [django-braces](https://django-braces.readthedocs.io/en/latest/#)
```cfgrlanguage
poetry add django-braces
```



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
> "channels" add without adding "daphne" to INSTALLED_APPS.

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

To integrate ```notebook``` with ```Django``` you need to install ```django-extensions```   
To run the notebook:
```cfgrlanguage
jupyter notebook
Новый / Django Shell-Plus
```

### [jupyterthemes](https://github.com/dunovank/jupyter-themes#install-with-pip)
```cfgrlanguage
poetry add --group dev jupyterthemes
```
#### [Command Line Usage jupyterthemes](https://github.com/dunovank/jupyter-themes#command-line-usage)
cl options| arg |default
|-|-|-|
List Themes| -l  |--
Theme Name to Install| -t  |--
> *list available themes*  
> jt -l  
>  
> *select theme...*  
> jt -t chesterish  

### Auto code completion [jupyter-tabnine](https://github.com/codota/jupyter-tabnine#installation)
```cfgrlanguage
poetry add --group dev jupyter_contrib_nbextensions
```
Do enable settings for user.  
Add without using poetry:
```cfgrlanguage
jupyter contrib nbextension install --user
```
Next:
```cfgrlanguage
poetry add --group dev jupyter_nbextensions_configurator
```
Do enable settings for user.  
Add without using poetry:
```cfgrlanguage
jupyter nbextensions_configurator enable --user
```
Do enable auto code completion in the settings of the running application jupiter.  
Go to menu "Nbextensions" and uncheck disable configuration for nbextensions.  
Сheck the box "Hinterland".  
End.
#### Run jupiter notebook:
```
poetry run python manage.py shell_plus --notebook
```
or
```cfgrlanguage
make shell
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

