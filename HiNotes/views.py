from django.shortcuts import render
from managenotes.models import Class

def home(request):
    classes = Class.objects.prefetch_related('subjects__notes').all()
    context = {'classes': classes}
    return render(request, "index.html", context)

def home_n(request, class_name):
    classes = Class.objects.prefetch_related('subjects__notes').all()
    context = {'classes': classes,'class_name': class_name,}
    return render(request, "home_n.html", context)