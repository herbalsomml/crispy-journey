# Generated by Django 5.0.4 on 2024-04-20 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersettings',
            old_name='owner',
            new_name='user',
        ),
    ]
