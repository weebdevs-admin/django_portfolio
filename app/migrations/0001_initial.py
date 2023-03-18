# Generated by Django 4.1.4 on 2023-03-03 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='Home')),
            ],
            options={
                'verbose_name': 'Home ',
                'verbose_name_plural': 'Home ',
            },
        ),
    ]