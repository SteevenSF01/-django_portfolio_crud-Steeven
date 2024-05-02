# Generated by Django 4.2.11 on 2024-05-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('icon', models.CharField(choices=[('bi-briefcase', 'Briefcase'), ('bi-card-checklist', 'Card Checklist'), ('bi-bar-chart', 'Bar Chart'), ('bi-binoculars', 'Binoculars'), ('bi-brightness-high', 'Brightness High'), ('bi-calendar4-week', 'Calendar Week')], default='bi-briefcase', max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
