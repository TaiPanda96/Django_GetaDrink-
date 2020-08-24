from django import forms
from .models import LCBO
from .models import Promotions

class LCBO_Form(forms.ModelForm):
    class Meta:
        model = LCBO
        fields = [
            'product',
            'price',
            'categories'

        ]
