# Generated by Django 4.2.2 on 2023-10-23 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='genre',
            field=models.CharField(choices=[('ROCK', 'Rock'), ('POP', 'Pop'), ('INDIE', 'Indie'), ('LOVE', 'Love')], max_length=30),
        ),
    ]
