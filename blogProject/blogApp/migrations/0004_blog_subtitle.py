# Generated by Django 5.1.2 on 2024-10-13 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_blog_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='subtitle',
            field=models.TextField(blank=True, null=True),
        ),
    ]
