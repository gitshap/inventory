from django.shortcuts import render
from django.http import HttpResponse
from equipment.models import Equipment


def hello(response):
    return HttpResponse('Hello')


def equipment_view(request, pk):
    equipment = Equipment.objects.get(id=pk)
    context = {
        'equipments': equipment,
    }
    template_name = 'equipment.html'
    return render(request, template_name, context=context)



