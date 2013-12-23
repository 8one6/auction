from django import forms

class WhoAmIForm(forms.Form):
    name = forms.CharField(max_length=200)