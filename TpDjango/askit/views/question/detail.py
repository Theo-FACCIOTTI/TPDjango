from django.views.generic import DetailView

from askit.models.question import Question


class QuestionDetailView(DetailView):
    template_name = 'question/detail.html'
    model = Question