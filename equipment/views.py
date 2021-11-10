from django.shortcuts import render
from equipment.models import Equipment
import csv


def home_view(request):
    template_name = 'home.html'

    total_equipment = Equipment.objects.all().count()

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


def equipment_view(request, label):
    equipment = Equipment.objects.get(label=label)
    context = {
        'equipments': equipment,
    }
    template_name = 'equipment.html'
    return render(request, template_name, context=context)
