# Generated by Django 4.1.1 on 2022-11-17 21:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('results', '0002_result_class_name_alter_result_filial_and_more'),
        ('userprofile', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_filial',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='results',
            field=models.ManyToManyField(to='results.result'),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students', models.ManyToManyField(related_name='%(app_label)s_%(class)s_related', to=settings.AUTH_USER_MODEL)),
                ('teacher_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
