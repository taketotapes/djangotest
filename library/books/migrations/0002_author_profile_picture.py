# Generated by Django 5.0 on 2023-12-20 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='books/profile_images'),
        ),
    ]