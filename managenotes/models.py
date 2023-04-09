from django.db import models

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):return f"Class {self.name}th"

class Subject(models.Model):
    name = models.CharField(max_length=50)
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='subjects')
    def __str__(self):return f"{self.class_field} {self.name}"

class Notes(models.Model):
    chapter_number = models.IntegerField()
    chapter_name = models.CharField(max_length=50)
    file = models.FileField(upload_to='notes/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='notes')
    def __str__(self):return f"{self.subject} Chapter {self.chapter_number}: {self.chapter_name}"
