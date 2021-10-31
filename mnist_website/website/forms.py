from django import forms 
from .models import User


class UserForm(forms.Form):
    class Meta:
        model = User
        fields = ('name', 'degree', 'age', 'region')
    name = forms.CharField(label='Name', max_length=100)
    degree = forms.CharField(label='Degree',max_length=150)
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'class': 'form-control typenumber', 'name': 'form-about-yourself', 'placeholder':'Age', 'id':'typenumber'}))
    region = forms.CharField(max_length=20) 
    
