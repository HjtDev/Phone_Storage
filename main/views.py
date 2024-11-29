from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db.models import Q, F
from .models import Phone
import pandas as pd
from django.core.serializers import serialize
from .models import Phone, Brand
import json
from .forms import PhoneForm


def index(request):
    return render(request, 'index.html')


def add_phone(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Check if the brand exists or create it
        brand_name = data.get('brand_name')
        brand, created = Brand.objects.get_or_create(name=brand_name)

        # Prepare data for the form
        form_data = {
            'brand': brand,
            'model': data.get('model'),
            'price': data.get('price'),
            'color': data.get('color'),
            'display_size': data.get('display_size'),
            'made_in': data.get('made_in'),
            'is_available': data.get('is_available', False)  # Ensure this is a boolean
        }

        form = PhoneForm(form_data)

        if form.is_valid():
            phone = form.save()
            return JsonResponse({'success': True, 'phone': {
                'id': phone.id,
                'brand': brand.name,
                'model': phone.model,
                'price': phone.price,
                'color': phone.color,
                'display_size': phone.display_size,
                'made_in': phone.made_in,
                'is_available': phone.is_available
            }})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': json.loads(errors)})


def phone_list(request):
    phones = Phone.objects.all()

    if 'search' in request.GET:
        search_query = request.GET['search']
        phones = phones.filter(
            Q(brand__name__icontains=search_query) |
            Q(brand__nationality__icontains=search_query) |
            Q(model__icontains=search_query) |
            Q(color__icontains=search_query) |
            Q(made_in__icontains=search_query)
        )

    if 'is_available' in request.GET:
        is_available = request.GET['is_available']
        phones = phones.filter(is_available=is_available)

    return render(request, 'phone_list.html', {'phones': phones})


def delete_phone(request, phone_id):
    if request.method == 'POST':
        phone = Phone.objects.get(id=phone_id)
        phone.delete()
        return JsonResponse({'success': True})


def export_to_json(request):
    phones = Phone.objects.all()

    if 'ids' in request.GET:
        ids = request.GET['ids'].split(',')
        phones = phones.filter(id__in=ids)

    data = serialize('json', phones)
    return JsonResponse(data, safe=False)


def export_to_excel(request):
    phones = Phone.objects.all()

    if 'ids' in request.GET:
        ids = request.GET['ids'].split(',')
        phones = phones.filter(id__in=ids)

    df = pd.DataFrame(list(phones.values()))

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="phones.xlsx"'

    df.to_excel(response, index=False)

    return response


def reports(request):
    korean_brands = Brand.objects.filter(country='Korea')
    phones_made_in_manufacturer_country = Phone.objects.filter(made_in=F('brand__country'))
    context = {
        'kb': korean_brands,
        'pmimc': phones_made_in_manufacturer_country,
    }
    return render(request, 'reports.html', context)

