from django import forms

class SearchForm(forms.Form):
    your_search = forms.CharField(label='q', max_length=50)