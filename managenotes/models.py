from django.db import models

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=4)
    name_word = models.CharField(max_length=32, default="")
    def __str__(self):return f"CLASS {self.name}th"

class Subject(models.Model):
    name = models.CharField(max_length=32)
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='subjects')
    def __str__(self):return f"{self.class_field} {self.name}"

class Notes(models.Model):
    chapter_number = models.CharField(max_length=8)
    chapter_name = models.CharField(max_length=64)
    file = models.FileField(upload_to='notes/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='notes')
    def __str__(self):return f"{self.subject} Chapter {self.chapter_number}: {self.chapter_name}"
