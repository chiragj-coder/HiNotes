from django.shortcuts import render
import pyrebase

config={
    "apiKey": "AIzaSyA4FIcyNcNjYP_Z8Ll4VyO4XAs23cVeL4E",
    "authDomain": "easenotes-cj.firebaseapp.com",
    "databaseURL": "https://easenotes-cj-default-rtdb.asia-southeast1.firebasedatabase.app/data",
    "projectId": "easenotes-cj",
    "storageBucket": "easenotes-cj.appspot.com",
    "messagingSenderId": "741857872370",
    "appId": "1:741857872370:web:f269e26efdd448b911836b"
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()


def home(request):

    # Get Class 9th & 10th Info
    class_9_10 = {
        'class_9':
            {
                'history':list(zip(get_chapters_name('class_9', 'history'), get_chapters_docs_path('class_9', 'history'))),
                'geography':list(zip(get_chapters_name('class_9', 'geography'), get_chapters_docs_path('class_9', 'geography'))),
                'civics':list(zip(get_chapters_name('class_9', 'civics'), get_chapters_docs_path('class_9', 'civics'))),
                'economics':list(zip(get_chapters_name('class_9', 'economics'), get_chapters_docs_path('class_9', 'economics'))),
            },
        'class_10':
            {
                'history':list(zip(get_chapters_name('class_10', 'history'), get_chapters_docs_path('class_10', 'history'))),
                'geography':list(zip(get_chapters_name('class_10', 'geography'), get_chapters_docs_path('class_10', 'geography'))),
                'civics':list(zip(get_chapters_name('class_10', 'civics'), get_chapters_docs_path('class_10', 'civics'))),
                'economics':list(zip(get_chapters_name('class_10', 'economics'), get_chapters_docs_path('class_10', 'economics')))
            }
    }

    # return render(request,"debug.html", class_9_10)
    return render(request,"Home.html", class_9_10)

def get_chapters_name(class_id, subject):
    chapters_id = list(database.child('class').child(class_id).child(subject).get().val())
    chapters_name = []
    for chapter_id in chapters_id:
        chapters_name.append(database.child('class').child(class_id).child(subject).child(chapter_id).child('chapter_name').get().val())
    return chapters_name

def get_chapters_docs_path(class_id, subject):
    chapters_id = list(database.child('class').child(class_id).child(subject).get().val())
    print(chapters_id)
    chapters_docs_path = []
    for chapter_id in chapters_id:
        chapters_docs_path.append(database.child('class').child(class_id).child(subject).child(chapter_id).child('docx').get().val())
    return chapters_docs_path