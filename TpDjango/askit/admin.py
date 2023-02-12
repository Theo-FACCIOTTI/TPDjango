from django.contrib import admin

from django.contrib import admin

from .models.answer import Answer
from .models.question import Question
from .models.score import Score
from .models.tag import Tag
from .models.topic import Topic

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Score)
admin.site.register(Tag)
admin.site.register(Topic)