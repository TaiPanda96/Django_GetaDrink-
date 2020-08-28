import django.shortcuts
from django.shortcuts import render
from django.http import response, request
from django.template import Template
from lcbo_app.models import LCBO
from lcbo_app.models import Promotions
from django.http import HttpResponseRedirect
from django.views.generic import (CreateView, DetailView, ListView, TemplateView,UpdateView)
from .forms import LCBO_Form


import get_byCategory
from get_byCategory import create_urls
from get_byCategory import to_map

import firebase
import firebase_admin 
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
    items      = get_dataset()

    item       = set([i['product']for i in items])
    item_price = set([i['price']for i in items])

    my_context = {
        'item' : item,
        'item_prices': item_price,
        'product' : product,
        'price'   : price,
    }
    return render(request,'lcbo_promos.html', my_context)


def favourites(request,*args,**kwargs):
    table = []
    url_list  = get_byCategory.create_urls()
    Product   = get_byCategory.retrieve_category('Product')
    Price     = get_byCategory.retrieve_category('Price')
    Category  = get_byCategory.retrieve_category('Category')

    table.append((Product,Price,Category))
    content   = {
        'Table'  :   table,
        'Product':   Product,
        'Price'  :   Price,
        'Category' : Category,
    }

    return render(request,'favourites.html',content)