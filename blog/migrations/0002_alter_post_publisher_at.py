# Generated by Django 5.0.1 on 2024-02-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publisher_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
