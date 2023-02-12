from django.views import generic
from django.urls import reverse

from askit.models.question import Question
from askit.forms.question_update import QuestionUpdateForm

class QuestionUpdateView(generic.FormView):
    model = Question
    template_name = 'question/update.html'
    form_class = QuestionUpdateForm

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            form.add_error(None, "User not authenticated")
            return reverse('login')
        text = form.cleaned_data['text']
        try:
            question = Question.objects.get(pk=self.kwargs['pk'])
            question.question_text = text
            question.save()
        except Exception as e:
            form.add_error(None, "Unexpected error")
            return super().form_invalid(form)
        return super().form_valid(form)
    
    def get_success_url(self):
        question_id = Question.objects.get(pk=self.kwargs['pk']).id
        return reverse('question_detail', kwargs={'pk': question_id})