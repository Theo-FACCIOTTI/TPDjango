from django.views.generic import ListView, FormView
from django.urls import reverse

from askit.models.topic import Topic
from askit.forms.search import SearchForm

class IndexView(ListView, FormView):
    template_name = 'index.html'
    Model = Topic
    form_class = SearchForm

    def get_queryset(self):
        return Topic.objects.all()

    def form_valid(self, form):
        search = form.cleaned_data['search']
        if search:
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('question_search', kwargs={'search': self.request.POST['search']})