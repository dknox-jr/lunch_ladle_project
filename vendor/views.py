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

factual = Factual('2ReKJ6iWVlbUs0B10VixjPGSMw1uLW5UQtL7tJgC', 'Xb0cE0OFsGp8zmGENU7j8T2hzoaNH9cpYvj80WKC')


@csrf_exempt
def scan(request):
    if request.method == "POST":
        upc = request.POST["scan"]
        data = {"KEY": "2ReKJ6iWVlbUs0B10VixjPGSMw1uLW5UQtL7tJgC", "q": upc, }
        params = urllib.urlencode(data)
#        f = "http://api.v3.factual.com/t/products-cpg-nutrition?select=product_name,%20ingredients"
        url = "http://api.v3.factual.com/t/products-cpg-nutrition?select=product_name,%20ingredients&" + params
        print url
#    return render(request, 'vendor/scan.html')
    return HttpResponse("<h1> it's alive!</hr>")