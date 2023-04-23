import csv

from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

import urllib.parse
from django.utils.safestring import mark_safe

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

def get_csv(request):
    from django.db.models import Q

    class_subjects = Subject.objects.all().select_related('class_field')

    notes = Notes.objects.filter(
        subject__in=class_subjects
    ).select_related('subject__class_field')

    data = []

    for note in notes:
        class_name = note.subject.class_field.name
        subject_name = note.subject.name
        chapter_number = note.chapter_number
        chapter_name = note.chapter_name
        file_url = mark_safe(urllib.parse.unquote(note.file.url))
        data.append(f'"{class_name}","{subject_name}","{chapter_number}","{chapter_name}","{file_url}"')
    db = str("<br>".join(data))
    return render(request, "display_db.html", {'db':db}, content_type='text/html; charset=utf-8')
    