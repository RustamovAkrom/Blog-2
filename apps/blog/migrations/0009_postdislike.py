# Generated by Django 5.1.1 on 2024-11-08 18:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_postcomment_post_alter_postlike_post_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostDislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='post_dislikes', to='blog.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_dislikes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
