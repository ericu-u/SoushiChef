from cProfile import label
from logging import PlaceHolder
from django import forms

class Search(forms.Form):
    search = forms.CharField(label=False,  widget=forms.TextInput(attrs={'placeholder': 'Search Foods...'}))

