# Generated by Django 3.2.14 on 2022-08-22 01:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('imgrec', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='imagefilemodel',
            name='user',
            field=models.ForeignKey(help_text='图库用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='图库用户'),
        ),
    ]
