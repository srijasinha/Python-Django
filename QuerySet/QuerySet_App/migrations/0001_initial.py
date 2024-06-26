# Generated by Django 5.0.1 on 2024-01-28 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('roll', models.ImageField(unique=True, upload_to='')),
                ('city', models.CharField(max_length=70)),
                ('marks', models.IntegerField()),
                ('pass_marks', models.DateField()),
            ],
        ),
    ]
