## [django_bootstrap5](https://django-bootstrap5.readthedocs.io/en/latest/index.html)
```cfgrlanguage
{% load django_bootstrap5 %}

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>{% block title %}{% endblock %}</title>
  
  {% bootstrap_css %}
  {% bootstrap_javascript %}
</head>
```


## [Django 4.2]()

Экранирование [safe](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#safe)

```
{{ post.content|safe }}
```

Форматирование даты [date](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#date)
```
{{ post.data_created|date:"SHORT_DATE_FORMAT" }}
```
