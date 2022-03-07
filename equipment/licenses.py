from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import transaction


from equipment.models import License, Staff
from equipment.forms import LicenseForm
from equipment.views import home_view




# create license
@transaction.atomic
def create_license(request):
    form = LicenseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(home_view)
        else:
            return HttpResponse("Wrong move")
    context = {
        'form': form
    }
    template_name = 'license/create_license.html'
    return render(request, template_name, context=context)
            
# assign/updating a license to a user
@transaction.atomic
def update_license(request, pk):
    specific_license = License.objects.get(id=pk)
    form = LicenseForm(request.POST or None, instance=specific_license)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.is_assigned = True
            instance.save()
            return redirect(home_view)
        else:
            return HttpResponse("Wrong move")
    context = {
        'form': form
    }
    template_name = 'license/create_license.html'
    return render(request, template_name, context=context)




# read license



# delete/unassigning license


