# Generated by Django 4.2.3 on 2023-07-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPegasus', '0007_photo_link_web_photo_text_inf_photo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='static/blog/img'),
        ),
    ]
