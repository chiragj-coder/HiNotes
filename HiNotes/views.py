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
    # class_9_10 = {
    #     'class_9':
    #         {
    #             'history':list(zip(get_chapters_name('class_9', 'history'), get_chapters_docs_path('class_9', 'history'))),
    #             'geography':list(zip(get_chapters_name('class_9', 'geography'), get_chapters_docs_path('class_9', 'geography'))),
    #             'civics':list(zip(get_chapters_name('class_9', 'civics'), get_chapters_docs_path('class_9', 'civics'))),
    #             'economics':list(zip(get_chapters_name('class_9', 'economics'), get_chapters_docs_path('class_9', 'economics'))),
    #         },
    #     'class_10':
    #         {
    #             'history':list(zip(get_chapters_name('class_10', 'history'), get_chapters_docs_path('class_10', 'history'))),
    #             'geography':list(zip(get_chapters_name('class_10', 'geography'), get_chapters_docs_path('class_10', 'geography'))),
    #             'civics':list(zip(get_chapters_name('class_10', 'civics'), get_chapters_docs_path('class_10', 'civics'))),
    #             'economics':list(zip(get_chapters_name('class_10', 'economics'), get_chapters_docs_path('class_10', 'economics')))
    #         }
    # }
    class_9_10 = {'class_9': {'history': [('The French Revolution', 'docs/class_9/history/1.pdf'), ('Socialism in Europe and the Russian Revolution', 'docs/class_9/history/2.pdf'), ('Nazism and the Rise of Hitler', 'docs/class_9/history/3.pdf'), ('Forest Society and Colonialism', 'docs/class_9/history/4.pdf'), ('Pastoralists in the Modern World', 'docs/class_9/history/5.pdf')], 'geography': [('India–Size and Location', 'docs/class_9/geography/1.pdf'), ('Physical Features of India', 'docs/class_9/geography/2.pdf'), ('Drainage', 'docs/class_9/geography/3.pdf'), ('Climate', 'docs/class_9/geography/4.pdf'), ('Natural Vegetation and Wildlife', 'docs/class_9/geography/5.pdf'), ('Population', 'docs/class_9/geography/6.pdf')], 'civics': [('What is Democracy? Why Is Democracy?', 'docs/class_9/civics/1.pdf'), ('Constitutional Design', 'docs/class_9/civics/2.pdf'), ('Electoral Politics', 'docs/class_9/civics/3.pdf'), ('Working of Institutions', 'docs/class_9/civics/4.pdf'), ('Democratic Rights ', 'docs/class_9/civics/5.pdf')], 'economics': [('The Story of Village Palampur', 'docs/class_9/economics/1.pdf'), ('People as Resource', 'docs/class_9/economics/2.pdf'), ('Poverty as a Challenge', 'docs/class_9/economics/3.pdf'), ('Food Security in India', 'docs/class_9/economics/4.pdf')]}, 'class_10': {'history': [('The Rise of Nationalism in Europe', 'docs/class_10/history/1.pdf'), ('Nationalism in India', 'docs/class_10/history/2.pdf'), ('The Making of a Global World', 'docs/class_10/history/3.pdf'), ('The Age of Industrialisation', 'docs/class_10/history/4.pdf'), ('Print Culture and the Modern World', 'docs/class_10/history/5.pdf')], 'geography': [('Resources and Development', 'docs/class_10/geography/1.pdf'), ('Forest and Wildlife Resources', 'docs/class_10/geography/2.pdf'), ('Water Resources', 'docs/class_10/geography/3.pdf'), ('Agriculture', 'docs/class_10/geography/4.pdf'), ('Minerals and Energy Resources', 'docs/class_10/geography/5.pdf'), ('Manufacturing Industries', 'docs/class_10/geography/6.pdf'), ('Lifelines of National Economy', 'docs/class_10/geography/7.pdf')], 'civics': [('Power-sharing', 'docs/class_10/civics/1.pdf'), ('Federalism', 'docs/class_10/civics/2.pdf'), ('Democracy and Diversity', 'docs/class_10/civics/3.pdf'), ('Gender, Religion and Caste', 'docs/class_10/civics/4.pdf'), ('Popular Struggles and Movements', 'docs/class_10/civics/5.pdf'), ('Political Parties', 'docs/class_10/civics/6.pdf'), ('Outcome Of Democracy', 'docs/class_10/civics/7.pdf'), ('Challenges to Democracy', 'docs/class_10/civics/8.pdf')], 'economics': [('Development', 'docs/class_10/economics/1.pdf'), ('Sectors of the Indian Economy', 'docs/class_10/economics/2.pdf'), ('Money and Credit', 'docs/class_10/economics/3.pdf'), ('Globalisation and the Indian Economy', 'docs/class_10/economics/4.pdf'), ('Consumer Rights', 'docs/class_10/economics/5.pdf')]}}
    print(class_9_10)

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