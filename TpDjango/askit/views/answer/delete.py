from django.urls import reverse
from django.views import generic

from askit.models.answer import Answer


class AnswerDeleteView(generic.DeleteView):
    model = Answer
    template_name = 'answer/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question_id'] = self.object.get_Question().id
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if(self.object.get_Question().question_user == self.request.user):
            self.object.delete()
        return super().delete(request, *args, **kwargs)
    

    def get_success_url(self):
        return reverse('question_detail', kwargs={'pk': self.object.get_Question().id})