# Generated by Django 5.1.2 on 2024-10-16 12:43

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0004_blog_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
    ]
