from django.shortcuts import render, redirect
from markupsafe import re
from equipment.models import Equipment, Licenses, Staff
from django.contrib.auth.decorators import permission_required
import csv
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm



def home_view(request):
    template_name = 'home.html'

    total_equipment = Equipment.objects.all().count()

    # TODO: Create recent view
    context = {
        'total_equipment': total_equipment,
    }

    return render(request, template_name, context=context)

def csv_to_import(request):
    with open('monitors.csv') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            Equipment.objects.create(
                name=row[0], label=row[1], location=row[2])
            line_count += 1
        print(f'Processed {line_count} lines.')
    return render(request, template_name='import_csv.html', context=None)

@permission_required('equipment.view_equipment', login_url='login_view')
def equipment_view(request, label):
    equipment = Equipment.objects.get(label=label)
    context = {
        'equipments': equipment,
    }
    template_name = 'equipment.html'
    return render(request, template_name, context=context)



def login_view(request):
    form = AuthenticationForm()
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(home_view)
    template_name = 'login.html' 
    context = {
        'form': form
    }
    return render(request, template_name, context=context)



def licenses_view(request):
    licenses = Licenses.objects.all()
    template_name = 'licenses.html'
    context = {
        'licenses': licenses
    }
    return render(request, template_name, context=context)