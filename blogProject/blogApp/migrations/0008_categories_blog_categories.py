# Generated by Django 5.1.2 on 2024-10-20 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0007_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(to='blogApp.categories'),
        ),
    ]
