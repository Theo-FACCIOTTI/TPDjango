from django import forms

class QuestionUpdateForm(forms.Form):
    text = forms.CharField(label="Text", min_length=5, max_length=500, widget=forms.Textarea(attrs={'rows': 5, 'cols': 20, 'style': 'height: 5em;'}), required=True)