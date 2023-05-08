from django.shortcuts import render
from managenotes.models import Class

def home(request):
    classes = Class.objects.prefetch_related('subjects__notes').all()
    context = {'classes': classes}
    return render(request, "home/index.html", context)

def dev(request):
    classes = Class.objects.prefetch_related('subjects__notes').all()
    context = {'classes': classes}
    return render(request, "dev/dev.html", context)