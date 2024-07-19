from django import forms

# Определяется форма для пользовательского ввода названия города

class CityForm(forms.Form):
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}))
