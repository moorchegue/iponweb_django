#-*- coding:utf-8 -*-

from decimal import Decimal
import random

from django.shortcuts import render, redirect

from realtdb.models import Realtor, House


def house_list(request):
    if request.method == "POST":
        random_realtor = random.choice(Realtor.objects.all())
        House.objects.create(
            realtor=random_realtor,
            address=request.POST['address'],
            area=float(request.POST['area']),
            price=Decimal(request.POST['price']))
        return redirect(request.path)

    house_list = House.objects.order_by('-id')
    return render(request, "realtdb/houses.html", {'house_list': house_list})
