# Generated by Django 5.1.1 on 2024-09-27 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test1_app', '0002_chattable_time_stamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chattable',
            old_name='message',
            new_name='mensagem',
        ),
        migrations.RenameField(
            model_name='chattable',
            old_name='sender',
            new_name='usuario',
        ),
    ]