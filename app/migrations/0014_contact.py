# Generated by Django 4.1.4 on 2023-03-17 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('education', models.CharField(max_length=200)),
                ('mobile_number', models.CharField(max_length=200)),
                ('languages', models.CharField(max_length=200)),
                ('instagram_link', models.CharField(max_length=300)),
                ('telegram_link', models.CharField(max_length=300)),
                ('github_link', models.CharField(max_length=300)),
                ('youtube_link', models.CharField(max_length=300)),
                ('button', models.CharField(max_length=30)),
            ],
        ),
    ]