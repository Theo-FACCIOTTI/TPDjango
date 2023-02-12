from django.views import generic
from django.urls import reverse
from django.contrib.auth.models import User

from askit.forms.profile import ProfileForm


class ProfileUpdateView(generic.FormView):
    model = User
    template_name = 'profile_update.html'
    form_class = ProfileForm

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            form.add_error(None, "User not authenticated")
            return reverse('login')
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        try:
            user = User.objects.get(pk=self.kwargs['pk'])
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        except Exception as e:
            form.add_error(None, "Unexpected error")
            return super().form_invalid(form)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.kwargs['pk']})
