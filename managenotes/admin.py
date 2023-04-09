from django.contrib import admin

# Register your models here.
from .models import Class, Subject, Notes
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Notes)