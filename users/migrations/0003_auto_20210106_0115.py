# Generated by Django 3.1 on 2021-01-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210105_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('english', 'english'), ('korean', 'korean')], max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='preference',
            field=models.TextField(blank=True, choices=[('movies', 'movies'), ('books', 'books')], max_length=10),
        ),
    ]