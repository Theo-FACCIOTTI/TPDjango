from django.views.generic import ListView

from askit.models.question import Question


class QuestionSearchView(ListView):
    model = Question
    template_name = 'question/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super().get_context_data(object_list=object_list, **kwargs)
        result['description_results'] = \
            "Search result of questions with title '{}'".format(self.kwargs['search'])
        return result

    def get_queryset(self):
        return Question.objects.filter(question_title__icontains=self.kwargs['search'])

class QuestionSearchByTopicView(ListView):
    model = Question
    template_name = 'question/list.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super().get_context_data(object_list=object_list, **kwargs)
        result['description_results'] = \
            "Search result of questions with topic '{}'".format(self.kwargs['topic_id'])
        return result

    def get_queryset(self):
        return Question.objects.filter(question_topic=self.kwargs['topic_id'])