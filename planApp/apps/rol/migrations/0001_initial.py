# Generated by Django 3.1.7 on 2021-03-03 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('config', models.TextField()),
                ('permissions', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(max_length=200)),
            ],
        ),
    ]