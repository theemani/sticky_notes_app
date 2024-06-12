# snasite/notes/views.py

from django.shortcuts import render, get_object_or_404
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Notes
from .forms import NotesForm
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .forms import NotesForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

# Create your views here.

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    """
    View to delete a note.
    """
    model = Notes  # Model used for deleting notes
    success_url = reverse_lazy("notes.list")  # Redirect URL after successful deletion
    template_name = "notes/notes_delete.html"  # Template to render
    login_url = "/login"

    def get_queryset(self):
        """
        Get the queryset of notes owned by the current user.
        """
        return self.request.user.notes.all()
    
    def get_object(self, queryset=None):
        """
        Get the note object to be deleted.
        Ensure that the current user owns the note.
        """
        return get_object_or_404(Notes, pk=self.kwargs.get('pk'), user=self.request.user)


class NotesUpdateView(LoginRequiredMixin, UpdateView):
    """
    View to update a note.
    """
    model = Notes  # Model used for updating notes
    success_url = reverse_lazy("notes.list")  # Redirect URL after successful update
    form_class = NotesForm  # Form class for updating notes
    login_url = "/login"

    def get_queryset(self):
        """
        Get the queryset of notes owned by the current user.
        """
        return self.request.user.notes.all()


class NotesCreateView(LoginRequiredMixin, CreateView):
    """
    View to create a new note.
    """
    model = Notes  # Model used for creating notes
    success_url = reverse_lazy("notes.list")  # Redirect URL after successful creation
    form_class = NotesForm  # Form class for creating notes
    login_url = "/login"

    def form_valid(self, form):
        """
        Save the form data, assign the note to the current user, and redirect to the success URL.
        """
        # Save the form data without committing to the database
        self.object = form.save(commit=False)
        # Assign the note to the current user
        self.object.user = self.request.user
        # Save the note
        self.object.save()
        # Redirect to the success URL
        return HttpResponseRedirect(self.get_success_url())


# To show the list of notes
class NotesListView(LoginRequiredMixin, ListView):
    """
    View to display a list of notes.
    """
    model = Notes  # Model used for displaying notes
    context_object_name = "notes"  # Context variable name for the list of notes
    login_url = "/login"

    def get_queryset(self):
        """
        Get the queryset of notes owned by the current user.
        """
        return self.request.user.notes.all()


# To show the content of the notes beyond the title
class NotesDetailView(LoginRequiredMixin, DetailView):
    """
    View to display the content of a note.
    """
    model = Notes  # Model used for displaying notes
    context_object_name = "note"  # Context variable name for the note object
    login_url = "/login"

    def get_queryset(self):
        """
        Get the queryset of notes owned by the current user.
        """
        return self.request.user.notes.all()
