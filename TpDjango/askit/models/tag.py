from django.db import models

class Tag(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name

    def get_fields(self):
        for field in self._meta.fields:
            if isinstance(field, models.ForeignKey):
                yield field.name, getattr(self, field.name).__str__()
            else:
                yield field.name, getattr(self, field.name)