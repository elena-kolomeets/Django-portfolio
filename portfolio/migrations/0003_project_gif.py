# Generated by Django 3.1.2 on 2020-11-04 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_github'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='gif',
            field=models.ImageField(default='C:/Users/Elena/Desktop/password_generator1', upload_to='portfolio/gifs/'),
            preserve_default=False,
        ),
    ]
