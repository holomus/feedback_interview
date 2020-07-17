from django.contrib.auth import authenticate, login

from Feedback_project.settings import LOGIN_REDIRECT_URL
from accounts.forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_view


# Create your views here.

class LoginView(auth_view.LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return '/admin'
        return LOGIN_REDIRECT_URL


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
        return redirect("feedback/create")
    else:
        form = RegistrationForm()

    return render(request, "accounts/register.html", {"form": form})
