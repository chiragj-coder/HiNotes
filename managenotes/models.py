from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=4)
    name_computing = models.CharField(max_length=4, default="")
    name_word = models.CharField(max_length=32, default="")
    is_hidden = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Class {self.name}th"

    class Meta:
        ordering = ['name_computing']

    @property
    def _class_name(self):
        hidden_str = " (hidden)" if self.is_hidden else ""
        return f"{self.__str__()}{hidden_str}"



class Subject(models.Model):
    name = models.CharField(max_length=32)
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='subjects')
    is_hidden = models.BooleanField(default=False)
    
    def __str__(self):
        hidden_str = " (hidden)" if self.is_hidden else ""
        return f"{self.class_field} {self.name}{hidden_str}"

    @property
    def _subject_name(self):
        hidden_str = " (hidden)" if self.is_hidden else ""
        return f"C{self.class_field.name} - {self.name}{hidden_str}"


 
class Notes(models.Model):
    chapter_number = models.CharField(max_length=8)
    chapter_name = models.CharField(max_length=64)
    file = models.FileField(upload_to='notes/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='notes')
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        hidden_str = " (hidden)" if self.is_hidden else ""
        try: return f"Chapter {int(self.chapter_number)}: {self.chapter_name}{hidden_str}"
        except: return f"Chapter {(self.chapter_number)}: {self.chapter_name}{hidden_str}"

    @property
    def _chapter_name(self):
        hidden_str = " (hidden)" if self.is_hidden else ""
        try: return f"Chapter {int(self.chapter_number)}: {self.chapter_name}{hidden_str}"
        except: return f"Chapter {(self.chapter_number)}: {self.chapter_name}{hidden_str}"