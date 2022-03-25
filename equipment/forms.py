from dataclasses import field
from django import forms
from django.forms import ModelForm
from equipment.models import Component, Consumable, License, Equipment
from crispy_forms.helper import FormHelper


class DateInput(forms.DateInput):
    input_type = 'date'



class CreateEquipmentForm(ModelForm):
    components = forms.ModelMultipleChoiceField(queryset=Component.objects.filter(in_use=False), required=False, widget=forms.SelectMultiple)
    class Meta:
        model = Equipment
        fields = ('name', 'status', 'asset_tag', 'date_purchased', 'date_deprecated', 'components')
        widgets = {
            'date_purchased': DateInput(),
            'date_deprecated': DateInput(),
            'asset_tag': forms.TextInput(attrs={'disabled': True}),

        }


    def __init__(self, *args, **kwargs):
        super(CreateEquipmentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'focus:outline-none w-96'})
        self.fields['asset_tag'].widget.attrs.update({'class': 'focus:outline-none w-96 disabled:opacity-75 select-none'})
        self.fields['status'].widget.attrs.update({'class': 'focus:outline-none w-96'})
        self.fields['date_purchased'].widget.attrs.update({'class': 'focus:outline-none w-96'})
        self.fields['date_deprecated'].widget.attrs.update({'class': 'focus:outline-none w-96'})
        self.fields['components'].widget.attrs.update({'class': 'focus:outline-none w-96'})
        self.fields['components'].required = False

        self.helper = FormHelper()


# License
class LicenseForm(ModelForm):
    class Meta:
        model = License
        fields = ('name', 'key', 'owner', )


class CreateConsumableForm(ModelForm):
    class Meta:
        model = Consumable
        fields = ('name', 'quantity')
    
    def __init__(self, *args, **kwargs):
        super(CreateConsumableForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'focus:outline-none w-96'})
        self.fields['quantity'].widget.attrs.update({'class': 'focus:outline-none w-96'})





class CheckoutForm(ModelForm):
    class Meta:
        model = Consumable
        fields = ('name', 'quantity', )
    
    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'type': 'hidden'})
        self.fields['quantity'].widget.attrs.update({'class': 'focus:outline-none w-96'})