from django import forms
from .models import Contact


#creating a form
class ContactForm(forms.ModelForm):

    #create metaclaass
    class Meta:
        #specify model to be use
        model = Contact
        #specify fields to be used
        fields = [
            "email",
            "subject",
            "message",
        ]

class PriceFilterForm(forms.Form):
    min_price = forms.DecimalField(label='Min Price', required=False)
    max_price = forms.DecimalField(label='Max Price', required=False)
