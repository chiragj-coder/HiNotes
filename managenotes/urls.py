from django.urls import path
from .views import upload_csv, get_csv

urlpatterns = [
    path('uploadcsv/', upload_csv, name='upload_csv'),
    path('getcsv/', get_csv, name='get_csv'),
]
