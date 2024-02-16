# Generated by Django 3.2.12 on 2024-02-13 18:52

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
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('avatar', models.FilePathField()),
                ('name', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32)),
                ('registr_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('text_message', models.CharField(max_length=512)),
                ('image', models.FilePathField()),
                ('message_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='render.users')),
            ],
        ),
    ]