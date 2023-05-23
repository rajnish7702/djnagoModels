from django import forms
class GeeksForms(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)