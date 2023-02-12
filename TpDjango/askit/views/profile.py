from django.views.generic import DetailView
from django.contrib.auth.models import User

class ProfileView(DetailView):
    template_name = 'profile.html'
    Model = User

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs['pk'])

    def get_score(self):
        return self.score_set.all()[0].score_value
    
    User.add_to_class('get_score', get_score)