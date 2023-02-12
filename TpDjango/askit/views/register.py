from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, login

from askit.forms.register import RegisterForm

class RegisterFormView(generic.FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            User.objects.create_user(
                username=username, email=email, password=password
            )
            messages.add_message(
                self.request, messages.INFO,
                'User created successfully.'
            )
        except Exception as e:
            form.add_error(None, "Unexpected error")
            return super().form_invalid(form)
        if form.is_valid():
            new_user = authenticate(username=username, password=password)
            login(self.request, new_user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')