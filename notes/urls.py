from django.urls import path
from .views import note_list, note_delete

urlpatterns = [
    path('',note_list,name='note_list'),
    path('note/<int:id>/delete', note_delete, name='note_delete')
]