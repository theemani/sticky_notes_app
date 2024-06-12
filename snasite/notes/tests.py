# snasite/notes/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Notes

class NotesModelTest(TestCase):

    def test_notes_creation(self):
        """
        Test that a note can be created with the expected title and content.
        """
        user = User.objects.create_user(username='testuser', password='12345')
        note = Notes.objects.create(title='Test Note', text='This is a test note.', user=user)
        self.assertEqual(note.title, 'Test Note')
        self.assertEqual(note.text, 'This is a test note.')
        self.assertEqual(note.user.username, 'testuser')

class NotesViewTest(TestCase):

    def setUp(self):
        """
        Set up a user and a note for the view tests.
        """
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.note = Notes.objects.create(title='Test Note', text='Test Note Content', user=self.user)

    def test_notes_list_view(self):
        """
        Test that the notes list view displays the note.
        """
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('notes.list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'Test Note Content')  # Ensure that both title and content are present

    def test_notes_detail_view(self):
        """
        Test that the notes detail view shows the correct note.
        """
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('notes.detail', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'Test Note Content')
