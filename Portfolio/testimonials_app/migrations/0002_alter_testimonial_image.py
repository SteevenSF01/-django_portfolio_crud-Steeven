# Generated by Django 4.2.11 on 2024-05-05 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(default='testimonials/default.jpg', upload_to='images/testimonials/'),
        ),
    ]