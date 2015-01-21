from django.shortcuts import render, render_to_response
from json import dumps, loads
from models import Purchase, Item, Ingredient
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from factual import Factual
from django.views.decorators.csrf import csrf_exempt
import urllib
import requests
import json

factual = Factual('2ReKJ6iWVlbUs0B10VixjPGSMw1uLW5UQtL7tJgC', 'Xb0cE0OFsGp8zmGENU7j8T2hzoaNH9cpYvj80WKC')


@csrf_exempt
def scan(request):
    if request.method == "POST":
        upc = request.POST["scan"]
        data = {"KEY": "2ReKJ6iWVlbUs0B10VixjPGSMw1uLW5UQtL7tJgC", "q": upc}
        params = urllib.urlencode(data)
        url = ("http://api.v3.factual.com/t/products-cpg-nutrition?select=product_name,%20ingredients&" +
               params)
        f = urllib.urlopen(url)
        # print (f.read())
        j = f.read()
        json_response = json.loads(j)
        print json_response
        product = json_response["response"]["data"][0]
        product_print = product["product_name"]
        ingredients = product["ingredients"]
        for ingredient in ingredients:
            print ingredient
            context = RequestContext(request)
            context_dict = {'product_name': product_print, 'product_code': upc}
            return render_to_response('vendor/scan.html', context_dict, context)

    return render(request, 'vendor/scan.html')


@csrf_exempt
def ajax(request):
    if request.method == "POST":

        item = Item()
        item.item_code = request.POST["item_code"]
        item.save()

    items = list(Item.objects.all())
    ajax_data = []
    for p in items:
        ingredients = []
        for i in p.ingredients.all():
            ingredients.append(i.ingredients)
        ajax_data.append({
            "scan": p.item_code,
            "item_name": p.item_name,
            "item_ingredients": ingredients,
        })

    return HttpResponse(dumps(ajax_data), content_type="application/json")


def dom(request):
    if request.method == "POST":
        print request.POST

    return render(request, 'vendor/scan.html')