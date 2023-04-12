# Generated by Django 3.2.18 on 2023-04-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managenotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='name',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='notes',
            name='chapter_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='notes',
            name='chapter_number',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]
