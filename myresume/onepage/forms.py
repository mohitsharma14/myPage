from django import forms
from onepage.models import UserContact

class NewUserForm(forms.ModelForm):
    class Meta:
        model = UserContact
        fields = '__all__'
