from django import forms
from main.models import Requester,Provider,OrderRequest

class CreateNewProvider(forms.Form):
    name = forms.CharField(label="Name",max_length=200)
    address = forms.CharField(label="Address", max_length=200)
    email = forms.CharField(label="Email", max_length=200)

class CreateNewRequest(forms.Form):
    requester = forms.ModelChoiceField(queryset=Requester.objects.all())
    provider = forms.ModelChoiceField(queryset=Provider.objects.all())
    quantity = forms.IntegerField()