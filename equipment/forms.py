from django.forms import ModelForm
from equipment.models import Consumable, License

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