
from django.core.validators import RegexValidator
from django import forms
from django.forms.models import ModelForm 
from .models import User, UserImage
from django.forms import inlineformset_factory
import re


def username_valid(username):
    pattern = re.compile('^[a-zA-Z0-9]([._-](?![._-])|[a-zA-Z0-9]){1,18}[a-zA-Z0-9]$')
    return pattern.match(username)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'username','degree', 'age')
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'type': 'text', 'name': 'name', 'placeholder': 'Your name...', 'required': 'required'})
        self.fields['username'].widget.attrs.update({'type': 'username', 'name': 'name', 'placeholder': 'Choose your unique username...', 'required': 'required'})
        self.fields['degree'].widget.attrs.update({'type': 'text', 'name': 'degree', 'placeholder': 'Degree...', 'required': 'required'})
        self.fields['age'].widget.attrs.update({'type': 'text', 'name': 'age', 'placeholder': 'Your age...', 'required': 'required'})
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username_valid(username):
            raise forms.ValidationError(u'Invalid Username')
        return username

class UserImageForm(forms.ModelForm):
    
    class Meta:
        model = UserImage
        fields = ('human_guess', 'image')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['human_guess'].widget.attrs.update({'type': 'number', 'name': 'human_guess', 'placeholder': 'Your best guess...!'})
        self.fields['human_guess'].required = False
        self.fields['human_guess'].widget.attrs['autofocus'] = 'on'
