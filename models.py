from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from django.urls import reverse

from firebase import get_dataset


# Models for Forms
LCBO_CHOICES = ( 
    ("1", "Beers & Cider"), 
    ("2", "Spirits"), 
    ("3", "Flavored Beer"), 
    ("4", "Ale"), 
    ("5", "Lagers"), 
    ("6", "Cocktails"),
) 

class LCBO(models.Model):
    # placeholder data
    product     = models.TextField(max_length=120, default=get_dataset()[1]['product'])
    price       = models.TextField(max_length=120, default=get_dataset()[1]['price'])
    categories  = models.CharField(max_length=120,choices=LCBO_CHOICES)


class Promotions(models.Model):
    available = 1
    out       = 2
    expired   = 3
    statuses  = (
        (available ,_('Available for Order')),
        (out       ,_('No Inventory')),
        (expired   ,_('No Longer on Sale')),
    )
    status = models.PositiveSmallIntegerField(
    choices=statuses,
    default=available,
    ) 


class Items(models.Model):
    item       =  models.TextField(max_length=120)
    item_price =  models.TextField(max_length=120)

    @classmethod
    def create_item(cls ,item,item_price):
        product = cls(item=item,item_price=item_price)
        return product