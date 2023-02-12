from django.db import models

from django.contrib.auth.models import User

class Score(models.Model):
    score_user = models.OneToOneField(User, on_delete=models.CASCADE)
    score_value = models.IntegerField(default=0)

    def __str__(self):
        return str(self.score_value)

    def get_fields(self):
        for field in self._meta.fields:
            if isinstance(field, models.ForeignKey):
                yield field.name, getattr(self, field.name).__str__()
            else:
                yield field.name, getattr(self, field.name)