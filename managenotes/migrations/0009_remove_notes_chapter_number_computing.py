# Generated by Django 3.2.18 on 2023-04-23 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managenotes', '0008_auto_20230423_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='chapter_number_computing',
        ),
    ]
