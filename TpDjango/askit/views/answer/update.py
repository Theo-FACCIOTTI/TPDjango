from django.views import generic
from django.urls import reverse

from askit.models.answer import Answer
from askit.forms.answer import AnswerForm

class AnswerUpdateView(generic.FormView):
    model = Answer
    template_name = 'answer/update.html'
    form_class = AnswerForm

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            form.add_error(None, "User not authenticated")
            return reverse('login')
        text = form.cleaned_data['text']
        try:
            answer = Answer.objects.get(pk=self.kwargs['pk'])
            answer.answer_text = text
            answer.save()
        except Exception as e:
            form.add_error(None, "Unexpected error")
            return super().form_invalid(form)
        return super().form_valid(form)
    
    def get_success_url(self):
        answer_question_id = Answer.objects.get(pk=self.kwargs['pk']).answer_question.id
        return reverse('question_detail', kwargs={'pk': answer_question_id})