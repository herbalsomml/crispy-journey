# Generated by Django 5.0.4 on 2024-04-20 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_customuser_has_license'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='has_license',
            field=models.BooleanField(default=True),
        ),
    ]
