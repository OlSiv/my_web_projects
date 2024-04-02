# Generated by Django 3.2.12 on 2024-03-15 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('nic', models.CharField(max_length=16)),
                ('avatar', models.FilePathField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32)),
                ('registr_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_message', models.CharField(max_length=512)),
                ('image', models.FilePathField()),
                ('message_time', models.DateTimeField()),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='render.users')),
            ],
        ),
    ]
