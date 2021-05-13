from django.db import models
from django.shortcuts import render
from django.utils.dateparse import parse_date
from django.shortcuts import render
from django.contrib import messages

from decimal import Decimal
import csv, io

from .models import Property
from .filter import SqftFilter

from django.views.generic import ListView
from django_filters.views import FilterView

# Create your views here.
def property_upload(request):
    template = "property/property_upload.html"

    if request.method == 'GET':
        return render(request, template)

    if request.method == 'POST':
        csv_file = request.FILES['file']

        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')

        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)

        for column in csv.reader(io_string, delimiter=','):
            if int(column[11]) < 1300000:
                pass
            else:

                property = Property.objects.create(
                    property_name = column[0],
                    property_sqft = int(column[1]),
                    city = column[2],
                    lease_number = column[3],
                    lease_type = column[4],
                    tenant_name = column[5],
                    unit_number = int(column[6]),
                    unit_sqft = int(column[7]),
                    lease_begin_date = parse_date(column[8]),
                    lease_end_date = parse_date(column[9]),
                    annual_rent_sqft =Decimal(column[10]),
                    annual_rent = int(column[11]),
                )
                property.save() 

    return render(request, template)



class PropertyList(ListView):
    model = Property

class FilterPropertyList(FilterView):
    model = Property
    context_object_name = 'property_list'
    template_name = 'property/property_filter.html'
    filterset_class = SqftFilter