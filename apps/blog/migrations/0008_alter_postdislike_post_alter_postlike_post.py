# Generated by Django 5.1.1 on 2024-11-10 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_alter_postcomment_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postdislike",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post_dislikes",
                to="blog.post",
            ),
        ),
        migrations.AlterField(
            model_name="postlike",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post_likes",
                to="blog.post",
            ),
        ),
    ]
