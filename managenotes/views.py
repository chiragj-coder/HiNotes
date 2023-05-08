import csv

from django.shortcuts import HttpResponse, render, redirect

from django.views.decorators.csrf import csrf_exempt

from .models import Notes, Class, Subject


@csrf_exempt
def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(decoded_file)
        for row in csv_reader:
            # Get or create the Class instance
            class_name = row['class']
            class_instance, _ = Class.objects.get_or_create(name=class_name)

            # Get or create the Subject instance
            subject_name = row['subject']
            subject_instance, _ = Subject.objects.get_or_create(name=subject_name, class_field=class_instance)

            # Create the Notes instance
            Notes.objects.create(
                chapter_number=row['chapter_number'],
                chapter_name=row['chapter_name'],
                file=row['file'],
                subject=subject_instance,
                is_hidden=row['is_hidden'] == 'True'
            )

        return redirect('/')  # Redirect to the home page after successful upload
    else:
        return render(request, 'mn/upload_csv.html')


def get_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="notes.csv"'
    
    # queryset of Notes objects
    notes = Notes.objects.all()

    # create a CSV writer
    writer = csv.writer(response)

    # write header row
    writer.writerow(['class', 'subject', 'is_hidden', 'chapter_number', 'chapter_name', 'file'])

    # write data rows
    for note in notes:
        writer.writerow([note.subject.class_field.name, note.subject.name, note.is_hidden, note.chapter_number, note.chapter_name, note.file.url])

    # send csv file
    return response