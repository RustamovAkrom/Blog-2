# Generated by Django 5.1.1 on 2024-11-13 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_description_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='description'),
        ),
    ]