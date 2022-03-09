from http.client import HTTPResponse
from django.shortcuts import render, redirect
from markupsafe import re
from equipment.models import Consumable, Equipment, License, Staff
from django.contrib.auth.decorators import permission_required
import csv
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CheckoutForm, CreateConsumableForm
from django.db.models import Q
from django.db import IntegrityError, transaction
from random import randint
from django.contrib import messages
from django.contrib.postgres.search import SearchHeadline, SearchQuery
from django.core.exceptions import ObjectDoesNotExist


def home_view(request):
    template_name = 'home.html'

    total_equipment = Equipment.objects.all().count()
    total_licenses = License.objects.all().count()
    get_shap_instance = Staff.objects.get(id=1)
    total_consumable_stock = Consumable.objects.filter(owner=get_shap_instance)
    total_consumable = 0
    for stock in total_consumable_stock:
        total_consumable += stock.quantity

    # TODO: Create recent view


    
    context = {
        'total_equipment': total_equipment,
        'total_license': total_licenses,
        'total_consumable': total_consumable
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
    licenses = License.objects.all()
    template_name = 'all_details/all_licenses.html'
    context = {
        'licenses': licenses
    }
    return render(request, template_name, context=context)


def list_equipments(request):
    equipments = Equipment.objects.all()
    template_name = 'all_details/all_equipment.html'
    context = {
        'equipments': equipments
    }
    return render(request, template_name, context=context)




def list_users(request):
    staffs = Staff.objects.all()
    template_name = 'staff/load_staff.html'
    context = {
        'staffs': staffs
    }
    return render(request, template_name, context=context)




# Consumables
def create_consumable(request):
    template_name = 'actions/create_consumable.html'
    get_shap_instance = Staff.objects.get(id=1)
    form = CreateConsumableForm(request.POST or None)
    if request.method == 'POST':
        form = CreateConsumableForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = get_shap_instance
            instance.save()
            messages.add_message(request, messages.SUCCESS, f'Consumable {instance.name} is created')
            print("huh")
            return redirect(view_consumable)
        else:
            messages.add_message(request, messages.ERROR, f'Quantity must not be negative')

    context = {
        'form': form
    }
    return render(request, template_name, context=context)


def view_consumable(request):
    template_name = 'consumables/load_consumables.html'
    shap_owner = Staff.objects.get(id=1)
    total_consumable_stock = Consumable.objects.filter(owner=shap_owner)
    total_consumable_deployed = Consumable.objects.filter(~Q(owner=shap_owner))
    total_consumable = 0
    total_deployed = 0
    for stock in total_consumable_stock:
        total_consumable += stock.quantity
    
    for stock in total_consumable_deployed:
        total_deployed += stock.quantity

    consumables = Consumable.objects.filter(owner=shap_owner)

    context = {
        'consumables': consumables,
        'total_consumable': total_consumable,
        'total_deployed': total_deployed
    }
    return render(request, template_name, context=context)

def update_consumable(request, id):
    template_name = 'consumables/update_consumable.html'
    consumable = Consumable.objects.get(id=id)
    form = CreateConsumableForm(request.POST or None, instance=consumable)
    if request.method == 'POST':
        form = CreateConsumableForm(request.POST or None, instance=consumable)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.add_message(request, messages.INFO, f'Consumable {instance.name} is updated')
            return redirect(view_consumable)
        else:
            messages.add_message(request, messages.ERROR, f'Consumable {instance.name} is not updated')
    context = {
        'form': form
    }
    return render(request, template_name, context=context)



def delete_consumable(request, id):
    template_name = 'consumables/delete_consumable.html'
    consumable = Consumable.objects.get(id=id)
    consumable.delete()
    context = {
        'consumable': consumable
    }
    return render(request, template_name, context=context)




# checkout view
@transaction.atomic
def checkout_consumable(request, id):
    template_name = 'consumables/checkout.html'
    random_id = randint(545, 500000005)
    get_shap = Staff.objects.get(id=1)
    # removing shap from the list
    staffs = Staff.objects.filter(~Q(id=get_shap.id))
    consumable = Consumable.objects.get(id=id)

    form = CheckoutForm(request.POST or None, instance=consumable)
    original_count = consumable.quantity
    try:
        if request.method == 'POST':
            if form.is_valid():
                form = CheckoutForm(request.POST or None, instance=consumable)
                instance = form.save(commit=False)
                get_owner_from_site = request.POST.get('staff')
                get_number_of_quantity = request.POST.get('quantity')
                get_owner_instance = Staff.objects.get(name=get_owner_from_site)
                print(get_owner_instance)
                try:
                    Consumable.objects.create(id=random_id, name=instance.name, quantity=get_number_of_quantity, owner=get_owner_instance)
                except IntegrityError:
                    Consumable.objects.create(id=random_id + random_id, name=instance.name, quantity=get_number_of_quantity, owner=get_owner_instance)
                instance.quantity = original_count - int(get_number_of_quantity)
                instance.save()
    
                return redirect(view_consumable)
            else:
                return redirect(view_consumable)
    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, f'User does not exist. Please try again')
        return redirect(view_consumable)


    context = {
        'form': form,
        'staffs': staffs,
        'consumable': consumable
    }
    return render(request, template_name, context=context)



# Staff
def staff_profile(request, id):
    template_name = 'staff/profile.html'
    staff = Staff.objects.get(id=id)
    assigned_consumables = Consumable.objects.filter(owner=staff)
    assigned_equipment = Equipment.objects.filter(owner=staff)
    context = {
        'staff': staff,
        'assigned_consumables': assigned_consumables,
        'assigned_equipment': assigned_equipment,
    }
    return render(request, template_name,  context=context)


def search_user(request):
    template_name = 'staff/search_staff.html'
    result_html = 'staff.results_staff.html'
    results = ''
    if request.method == 'POST':
        query = request.POST.get('search', '1')
        searched_query = SearchQuery(query)

        search_headline = SearchHeadline("name", searched_query,
        start_sel='<b>',
        stop_sel='</b>')

        results = Staff.objects.annotate(
            headline=search_headline,
        ).filter(name__search=searched_query)

       
        context = {
            'results': results,
        }

        return render( request, result_html, context=context)
    else:
        context = {
            'result': '1'
        }
        return render(request, template_name, context=context)