# Generated by Django 3.2.18 on 2023-04-09 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('class_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='managenotes.class')),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_number', models.IntegerField()),
                ('chapter_name', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='notes/')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='managenotes.subject')),
            ],
        ),
    ]
