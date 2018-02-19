from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True,label='Your mail')
    subject = forms.CharField(required=True,label='The subject')
    message = forms.CharField(widget=forms.Textarea, required=True,label='Message')

