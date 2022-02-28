from django.forms import ModelForm
from equipment.models import License

# License
class LicenseForm(ModelForm):
    class Meta:
        model = License
        fields = ('name', 'key', 'owner', )
