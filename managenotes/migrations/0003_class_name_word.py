# Generated by Django 3.2.18 on 2023-04-16 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managenotes', '0002_auto_20230412_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='name_word',
            field=models.CharField(default='', max_length=32),
        ),
    ]