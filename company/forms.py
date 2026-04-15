from django import forms
from .models import Contact, Newsletter
from django.forms import ModelForm


class ContactForm(forms.ModelForm):
    """ Fields for contact form """
    name = forms.CharField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    email = forms.EmailField(
        max_length=100, widget=forms.EmailInput(
            attrs={'class': 'form-control'}))
    subject = forms.CharField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder':
                            'Write your message here!'}))

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Eneter your Name..'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Eneter your Email..'})
