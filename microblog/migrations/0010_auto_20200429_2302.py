# Generated by Django 3.0.5 on 2020-04-29 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0009_auto_20200429_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
