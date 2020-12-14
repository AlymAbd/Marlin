from django.shortcuts import render
from . import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from products.models import Prices

# Create your views here.

@api_view(['POST'])
def create_order(request):
    jsone = json.loads(request.data)

    for product in jsone.get('products'):
        price_id = product.get('price_id')
        count = product.get('quant')
        price = Prices.objects.get(pk=price_id).price
        jsone['total_amount'] += (count*price)
    
    
    user_id = jsone.get('user_id')
    obj = models.Order.objects.create(
        amount=count*
    )
