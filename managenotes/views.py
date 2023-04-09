import csv

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Notes, Class, Subject

@csrf_exempt
def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()

        reader = csv.DictReader(decoded_file)
        for row in reader:
            subject_name = row['subject']
            class_name = row['class']
            chapter_number = row['chapter_number']
            chapter_name = row['chapter_name']
            file = row['file']

            class_obj, created = Class.objects.get_or_create(name=class_name)
            subject_obj, created = Subject.objects.get_or_create(name=subject_name, class_field=class_obj)
            Notes.objects.create(chapter_number=chapter_number, chapter_name=chapter_name, file=file, subject=subject_obj)

    return render(request, 'upload_csv.html')
