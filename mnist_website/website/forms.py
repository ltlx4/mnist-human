from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms.widgets import Textarea 
from django.forms import * 
from django.forms.models import ModelForm 
from .models import User, UserImage





class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('name', 'degree', 'age')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'type': 'text', 'name': 'name', 'placeholder': 'Your name...', 'required': 'required'})
        self.fields['degree'].widget.attrs.update({'type': 'text', 'name': 'degree', 'placeholder': 'Degree...', 'required': 'required'})
        self.fields['age'].widget.attrs.update({'type': 'text', 'name': 'age', 'placeholder': 'Your age...', 'required': 'required'})
    

class UserImageForm(ModelForm):
    
    class Meta:
        model = UserImage
        fields = ('image', 'human_guess', 'real_value',)

