from django import forms

from askit.models.topic import Topic

class QuestionForm(forms.Form):
    title = forms.CharField(label="Title", min_length=5, max_length=50, required=True)
    text = forms.CharField(label="Text", min_length=5, max_length=500, widget=forms.Textarea(attrs={'rows': 5, 'cols': 20, 'style': 'height: 5em;'}), required=True)
    topic = forms.ModelChoiceField(queryset=Topic.objects.all(), empty_label="Select a topic", to_field_name="topic_name", label="Topic", required=True)