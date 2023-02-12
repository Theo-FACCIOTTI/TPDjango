from django.db import models

from .tag import Tag
from django.contrib.auth.models import User
from .topic import Topic


class Question(models.Model):
    question_title = models.CharField(max_length=50)
    question_text = models.CharField(max_length=500)
    question_date = models.DateTimeField('date published')
    question_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question_topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    question_tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.question_title

    def get_fields(self):
        for field in self._meta.fields:
            if isinstance(field, models.ForeignKey):
                yield field.name, getattr(self, field.name).__str__()
            else:
                yield field.name, getattr(self, field.name)
    
    def get_Answers(self):
        return self.answer_set.all()

    def get_Tags(self):
        return self.question_tag.all()

    def get_Author(self):
        return self.question_user
                