# Generated by Django 4.2.11 on 2024-05-31 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_alter_portfolioitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioitem',
            name='category',
            field=models.CharField(choices=[('app', 'app'), ('card', 'card'), ('web', 'web')], max_length=10),
        ),
    ]