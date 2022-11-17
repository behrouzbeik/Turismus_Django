from django import forms

class ServicesLoaderForm (forms.Form):
    destination = forms.CharField(max_length=50)
    departDate = forms.DateField
    returnDate = forms.DateField
    service = forms.CharField(max_length=10)