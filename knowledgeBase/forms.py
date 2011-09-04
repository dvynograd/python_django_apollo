from django import forms

class MemoCommentForm(forms.Form):
    subject = forms.CharField(max_length=100)
    description = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)