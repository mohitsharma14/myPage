from django import forms
from onepage.models import UserContact

class NewUserForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    email = forms.CharField(widget = forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    subject = forms.CharField(widget = forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    message = forms.CharField(widget = forms.Textarea(
        attrs={
            'class': 'form-control',
        }
    ))
    class Meta:
        model = UserContact
        fields = ['name', 'email', 'subject', 'message']
