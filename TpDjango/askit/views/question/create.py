from django.contrib import messages
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from askit.forms.question import QuestionForm
from askit.models.question import Question

class QuestionFormView(generic.FormView):
    template_name = 'question/create.html'
    form_class = QuestionForm

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            form.add_error(None, "User not authenticated")
            return reverse('login')
        title = form.cleaned_data['title']
        text = form.cleaned_data['text']
        topic = form.cleaned_data['topic']
        try:
            Question.objects.create(
                question_title=title, question_text=text, question_user=self.request.user, question_topic=topic, question_date=timezone.now()
            )
            messages.add_message(
                self.request, messages.INFO,
                'Question created successfully.'
            )
        except Exception as e:
            form.add_error(None, "Unexpected error")
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('question_list')