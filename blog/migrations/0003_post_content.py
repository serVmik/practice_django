# Generated by Django 4.2.8 on 2023-12-18 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
