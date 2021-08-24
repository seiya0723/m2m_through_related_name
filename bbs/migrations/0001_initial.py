# Generated by Django 3.1.2 on 2021-08-19 05:03

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
            name='BadTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='悪いねした時刻')),
            ],
            options={
                'db_table': 'bad_topic',
            },
        ),
        migrations.CreateModel(
            name='GoodTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='良いねした時刻')),
            ],
            options={
                'db_table': 'good_topic',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日')),
                ('comment', models.CharField(max_length=200, verbose_name='コメント')),
                ('bad', models.ManyToManyField(related_name='posted_bad', through='bbs.BadTopic', to=settings.AUTH_USER_MODEL, verbose_name='悪いね')),
                ('good', models.ManyToManyField(related_name='posted_good', through='bbs.GoodTopic', to=settings.AUTH_USER_MODEL, verbose_name='良いね')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted_user', to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
            ],
            options={
                'db_table': 'topic',
            },
        ),
        migrations.AddField(
            model_name='goodtopic',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.topic', verbose_name='良いねしたトピック'),
        ),
        migrations.AddField(
            model_name='goodtopic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='良いねしたユーザー'),
        ),
        migrations.AddField(
            model_name='badtopic',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.topic', verbose_name='悪いねしたトピック'),
        ),
        migrations.AddField(
            model_name='badtopic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='悪いねしたユーザー'),
        ),
    ]