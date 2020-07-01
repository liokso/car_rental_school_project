from django import forms
from customers.models import *

class CarInformationForm(forms.Form):
	search_condition = forms.CharField()

class GeneralSearchForm(forms.Form):
	search_condition = forms.CharField()