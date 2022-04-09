from django import forms


class CityForm(forms.Form):
    name_city = forms.CharField(label='Название города', widget=forms.TextInput(attrs={
        'placeholder': 'Введите название города',
        'class': 'form-control'
    }))
