# Generated by Django 3.2.18 on 2023-04-23 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managenotes', '0010_subject_is_hidden'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='is_hidden',
            field=models.BooleanField(default=False),
        ),
    ]