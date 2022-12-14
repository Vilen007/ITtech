# Generated by Django 3.1.6 on 2021-03-19 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=250)),
                ('content', models.TextField()),
                ('author', models.CharField(default='', max_length=50)),
                ('slug', models.CharField(default='', max_length=130)),
                ('timestump', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='blogs_comment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('timestump', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogs_comment')),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
