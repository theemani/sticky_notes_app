from django.urls import path
from . import views

urlpatterns = [
    # URL patterns for Notes app
    path("notes/", views.NotesListView.as_view(), name="notes.list"),  # List view for notes
    path("notes/<int:pk>", views.NotesDetailView.as_view(), name="notes.detail"),  # Detail view for a specific note
    path("notes/<int:pk>/edit", views.NotesUpdateView.as_view(), name="notes.update"),  # Update view for a specific note
    path("notes/<int:pk>/delete", views.NotesDeleteView.as_view(), name="notes.delete"),  # Delete view for a specific note
    path("notes/new", views.NotesCreateView.as_view(), name="notes.new"),  # Create view for new notes
]
