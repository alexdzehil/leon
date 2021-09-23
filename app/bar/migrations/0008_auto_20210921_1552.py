# Generated by Django 3.2.7 on 2021-09-21 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0007_auto_20210921_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpageconfig',
            name='menu_title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Заголовок меню'),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Подзаголовок меню')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото меню')),
                ('config', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bar.mainpageconfig')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
    ]
