# Generated by Django 5.0.4 on 2024-04-20 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('fanclubJoin', 'Fan Club Join'), ('follow', 'Follow'), ('mediaPurchase', 'Media Purchase'), ('tip', 'Tip'), ('unfollow', 'Unfollow'), ('userEnter', 'User Enter'), ('userLeave', 'User Leave')], max_length=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='received_at',
            field=models.DateTimeField(),
        ),
    ]
