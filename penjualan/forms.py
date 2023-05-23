from django import forms
from .models import MyModel

class MyModelForm(forms.ModelForm):
    tgltrans = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = MyModel
        fields = ['kdbrg', 'nmbrg', 'tgltrans', 'jumbrg', 'hargabrg', 'totalbyr']
