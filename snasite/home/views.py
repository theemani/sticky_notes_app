from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect

from django.http import HttpResponseRedirect

# Create your views here.

class SignupView(CreateView):
    """
    View for user registration/signup.
    """
    form_class = UserCreationForm  # Form class for user registration
    template_name = "home/register.html"  # Template for the registration page
    success_url = "/smart/notes/"  # URL to redirect after successful registration

    def get(self, request, *args, **kwargs):
        """
        Override get method to redirect authenticated users.
        """
        if self.request.user.is_authenticated:
            # Redirect authenticated users to the notes list page
            return redirect("notes.list")
        return super().get(request, *args, **kwargs)


class LoginInterfaceView(LoginView):
    """
    View for user login.
    """
    template_name = "home/login.html"  # Template for the login page


class LogoutInterfaceView(LogoutView):
    """
    View for user logout.
    """
    template_name = "home/logout.html"  # Template for the logout page


class HomeView(TemplateView):
    """
    View for home/welcome page.
    """
    template_name = "home/welcome.html"  # Template for the home/welcome page

# Authorised/Restricted if logged in shows the
# authorised.html page
# if logged out redirects to the login page
