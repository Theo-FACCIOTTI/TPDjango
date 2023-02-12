from django.views.generic import ListView

from askit.models.question import Question


class QuestionListView(ListView):
    template_name = 'question/list.html'
    model = Question