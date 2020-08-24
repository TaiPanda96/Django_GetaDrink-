import django.shortcuts
from django.shortcuts import render
from django.http import response, request
from django.template import Template
from lcbo_app.models import LCBO
from lcbo_app.models import Promotions
from django.http import HttpResponseRedirect
from django.views.generic import (CreateView, DetailView, ListView, TemplateView,UpdateView)
from .forms import LCBO_Form


import firebase
import firebase_admin 
from firebase import get_dataset
from firebase import get_dataset
from firebase_admin import credentials
cred = credentials.Certificate("/Users/taishanlin/Desktop/django_lcbo/lcbo_app/lcbo-26e4f-firebase-adminsdk-4yat0-88c203027f.json")

from lcbo_app.models import LCBO
import datetime
from datetime import time, timezone, date



def home(request):
    return render(request,'home.html')

def index(request):
    return render(request, 'index.html')

def lcbo_promos(request, *args, **kwargs):
    category   = LCBO_Form()
    product    = get_dataset()[5]['product']
    price      = get_dataset()[5]['price']
    date       = datetime.date.today()
    sys_date   =  date.strftime("%d/%m/%Y")
    items      = get_dataset()
    item       = set([i['product']for i in items])
    item_price = set([i['price']for i in items])
    my_context = {
        'item' : item,
        'item_prices': item_price,
        'product' : product,
        'price'   : price,
        'date'    : sys_date,
    }
    return render(request,'lcbo_promos.html', my_context)
