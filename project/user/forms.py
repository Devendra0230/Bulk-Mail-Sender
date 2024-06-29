from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import receiverFileModel,senderFileModel


CHOICES = {465: "465 (Secure - Recommended)"}


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username', 'password1', 'password2'
        ]

class senderFileForm(forms.ModelForm):
    class Meta:
        model = senderFileModel
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(senderFileForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs['accept'] = '.csv, .txt'
        self.fields['file'].widget.attrs['class'] = 'form-control'
        self.fields['esp'].widget.attrs['class'] = 'form-control'
        self.fields['esp'].widget.attrs['placeholder'] = 'ex. mail.geeektheo.com'
        self.fields['port'].widget=forms.RadioSelect(choices = CHOICES)

class receiverFileForm(forms.ModelForm):
    class Meta:
        model = receiverFileModel
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(receiverFileForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs['class'] = 'form-control'
        self.fields['file'].widget.attrs['accept'] = '.csv, .txt'





