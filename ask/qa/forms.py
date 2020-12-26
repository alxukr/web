from django import forms

class AnswerForm(forms.Form):
    text = forms.CharField(widget = forms.Textarea)
    question = forms.CharField(max_length = 100)

class AskForm(forms.Form):
    title = forms.CharField(max_length = 50)
    text = forms.CharField(widget = forms.Textarea)

