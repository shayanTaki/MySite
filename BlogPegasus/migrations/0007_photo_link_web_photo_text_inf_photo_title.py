# Generated by Django 4.2.3 on 2023-07-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPegasus', '0006_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='link_web',
            field=models.CharField(default='hi', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='text_inf',
            field=models.CharField(default='hi', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
