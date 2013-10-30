#-*- coding:utf-8 -*-

from decimal import Decimal
import random

from django.shortcuts import render, redirect
from django import forms

from realtdb.models import Realtor, House, Apartment


class HouseForm(forms.Form):
    address = forms.CharField(max_length=100)
    area = forms.IntegerField()
    price = forms.IntegerField()


class ApartmentForm(HouseForm):
    rooms = forms.IntegerField()
    floor = forms.IntegerField()
    floors = forms.IntegerField()


def house_list(request):
    result = {}

    if request.method == "POST":
        form = HouseForm(request.POST)
        if form.is_valid():
            random_realtor = random.choice(Realtor.objects.all())
            House.objects.create(
                realtor=random_realtor,
                address=request.POST['address'],
                area=float(request.POST['area']),
                price=Decimal(request.POST['price']))
            return redirect(request.path)
        else:
            result['error'] = 'Form validation error'

    result['house_list'] = House.objects.order_by('-id')
    return render(request, "realtdb/houses.html", result)


def apartment_list(request):
    result = {}

    if request.method == "POST":
        form = ApartmentForm(request.POST)
        if form.is_valid():
            random_realtor = random.choice(Realtor.objects.all())
            Apartment.objects.create(
                realtor=random_realtor,
                address=request.POST['address'],
                area=float(request.POST['area']),
                price=Decimal(request.POST['price']),
                rooms=int(request.POST['rooms']),
                floor=int(request.POST['floor']),
                floors=int(request.POST['floors']),
            )
            return redirect(request.path)
        else:
            result['error'] = 'Form validation error'

    result['apartment_list'] = Apartment.objects.order_by('-id')
    return render(request, "realtdb/apartments.html", result)
