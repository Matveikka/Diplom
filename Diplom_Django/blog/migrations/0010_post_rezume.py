# Generated by Django 4.2.17 on 2024-12-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rezume',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
