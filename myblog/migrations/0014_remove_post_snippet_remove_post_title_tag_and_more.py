# Generated by Django 4.2.3 on 2023-08-14 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myblog', '0013_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='snippet',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_tag',
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
