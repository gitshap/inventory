from django.shortcuts import redirect, render
from equipment.forms import CreateConsumableForm, CreateEquipmentForm

from equipment.models import Staff, Equipment, Component
from equipment.views import view_consumable
from django.contrib import messages


def create_equipment(request):
    template_name = 'equipments/create_equipment.html'
    get_shap_instance = Staff.objects.get(id=1)
    form = CreateEquipmentForm(request.POST or None)
    if request.method == 'POST':
        form = CreateEquipmentForm(request.POST or None)
        
        if form.is_valid():
            picked = form.cleaned_data.get('components')
            instance = form.save(commit=False)
            instance.owner = get_shap_instance
            instance.save()
            print('form is valid')
            for pick in picked:
                instance.components.add(pick)
                pick.in_use = True
                pick.save()
            messages.add_message(request, messages.SUCCESS, f'Equipment {instance.name} is created')
            print("Created")
            return redirect(view_consumable)
        else:
            print('form is invalid')
            messages.add_message(request, messages.ERROR, f'Quantity must not be negative')

    context = {
        'form': form
    }
    return render(request, template_name, context=context)