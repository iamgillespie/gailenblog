# Generated by Django 4.0.5 on 2022-06-12 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=models.TextField(max_length=280),
        ),
    ]