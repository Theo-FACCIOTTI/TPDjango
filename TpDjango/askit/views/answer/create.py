from django.views import generic
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone

from askit.forms.answer import AnswerForm
from askit.models.answer import Answer
from askit.models.question import Question

class AnswerFormView(generic.FormView):
    template_name = 'answer/create.html'
    form_class = AnswerForm

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            form.add_error(None, "User not authenticated")
            return reverse('login')
        text = form.cleaned_data['text']
        try:
            Answer.objects.create(
                answer_text=text,
                answer_user=self.request.user,
                answer_question=Question.objects.get(pk=self.kwargs['question_id']),
                answer_date=timezone.now(),
                answer_answer=Answer.objects.get(pk=self.kwargs['answer_id']) if 'answer_id' in self.kwargs else None
            )
            messages.add_message(
                self.request, messages.INFO,
                'Answer created successfully.'
            )
        except Exception as e:
            form.add_error(None, "Unexpected error")
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('question_detail', kwargs={'pk': self.kwargs['question_id']})