# Generated by Django 5.2.3 on 2025-06-24 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]
