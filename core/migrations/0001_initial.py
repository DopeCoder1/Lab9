# Generated by Django 4.0.3 on 2022-04-06 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя автора')),
                ('phone', models.CharField(max_length=255)),
                ('emails', models.EmailField(max_length=254)),
                ('mssg', models.TextField()),
                ('dates', models.DateField()),
            ],
        ),
    ]
