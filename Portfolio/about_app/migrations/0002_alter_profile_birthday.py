# Generated by Django 4.2.11 on 2024-05-03 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.TextField(),
        ),
    ]
