from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name="home"),
    path('notes',views.notes, name="notes"),
    path('delete_note/<int:pk>',views.delete_note, name="delete-note"),
    path('notes/<int:pk>/', views.NotesDetailView.as_view(), name='note-detail'),
    path('homework',views.homework, name="homework"),
    path('update_homework/<int:pk>/', views.update_homework, name='update-homework')
]

