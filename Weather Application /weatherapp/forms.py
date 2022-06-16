
from django import forms
from django.forms import ModelForm, TextInput


from weatherapp.models import CityName


class NewForm(ModelForm):

    class Meta:
        model = CityName
        fields = "__all__"
        widgets = {'contentInside': TextInput( attrs={'class':'input', 'placeholder' : 'Enter a City Name' } ) }
        # fields = ("contentInside")