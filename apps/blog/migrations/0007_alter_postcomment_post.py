# Generated by Django 5.1.1 on 2024-11-10 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_postcomment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='blog.post'),
        ),
    ]
