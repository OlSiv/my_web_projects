# Generated by Django 3.2.12 on 2024-06-17 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('render', '0003_alter_message_time_sent_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='time_sent_at',
            new_name='message_time',
        ),
    ]
