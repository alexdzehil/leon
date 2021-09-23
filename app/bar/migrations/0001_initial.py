# Generated by Django 3.2.7 on 2021-09-20 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainPageConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_title', models.CharField(max_length=100)),
                ('gallery_title', models.CharField(max_length=15)),
                ('about_title', models.CharField(max_length=15)),
                ('contacts_title', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Конфигурация сайта',
            },
        ),
    ]
