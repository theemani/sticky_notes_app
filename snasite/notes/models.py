# snasite/notes/model.py

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    """
    Model to represent a note.
    """
    title = models.CharField(max_length=200)  # Title of the note
    text = models.TextField()  # Content of the note
    created = models.DateTimeField(auto_now_add=True)  # Date and time when the note was created
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")  # User who owns the note
