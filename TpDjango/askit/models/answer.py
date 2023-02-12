from django.db import models

from .question import Question
from .tag import Tag
from django.contrib.auth.models import User

class Answer(models.Model):
    answer_text = models.CharField(max_length=500)
    answer_date = models.DateTimeField('date published')
    answer_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    answer_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_answer = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    answer_tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.answer_text
    
    def get_fields(self):
        for field in self._meta.fields:
            if isinstance(field, models.ForeignKey):
                yield field.name, getattr(self, field.name).__str__()
            else:
                yield field.name, getattr(self, field.name)
    
    def get_Tags(self):
        return self.answer_tag.all()

    def get_Author(self):
        return self.answer_user

    def get_Question(self):
        return self.answer_question