from django.db import models

class Topic(models.Model):
    topic_name = models.CharField(max_length=20)

    def __str__(self):
        return self.topic_name

    def get_fields(self):
        for field in self._meta.fields:
            if isinstance(field, models.ForeignKey):
                yield field.name, getattr(self, field.name).__str__()
            else:
                yield field.name, getattr(self, field.name)