# Generated by Django 3.2.12 on 2024-03-15 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('render', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='users',
            new_name='user',
        ),
    ]