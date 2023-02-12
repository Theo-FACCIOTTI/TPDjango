from django import forms

class AnswerForm(forms.Form):
    text = forms.CharField(label="Answer", max_length=500, widget=forms.Textarea(attrs={'rows': 5, 'cols': 20, 'style': 'height: 5em;'}), required=True)
