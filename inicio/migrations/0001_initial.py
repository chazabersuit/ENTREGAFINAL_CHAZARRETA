# Generated by Django 4.0.6 on 2022-07-30 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=15)),
                ('subtitulo', models.CharField(max_length=30)),
                ('contenido', models.CharField(max_length=100)),
            ],
        ),
    ]
