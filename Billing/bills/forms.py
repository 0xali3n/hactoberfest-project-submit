from django import forms
from django.contrib.auth import get_user_model

class InfoForm(forms.Form):
    customername = forms.CharField(widget=forms.TextInput(
			attrs={"class":"form-control",
			"placeholder":"Customer Name",
			'name': 'display_name'
			}
			))

    customerid = forms.CharField(widget=forms.TextInput(
			attrs={"class":"form-control",
			"placeholder":"Customer ID",
			'name': 'display_name'
			}
			),required=False)
	
    mobilenumber = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control",
               "placeholder": "Your Mobile Number"
               }
    ))
