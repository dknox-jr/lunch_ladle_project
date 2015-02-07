from django.shortcuts import render, render_to_response
from json import dumps, loads
from models import Purchase, Item, Ingredient
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from forms import ItemForm
from factual import Factual
factual = Factual('2ReKJ6iWVlbUs0B10VixjPGSMw1uLW5UQtL7tJgC', 'Xb0cE0OFsGp8zmGENU7j8T2hzoaNH9cpYvj80WKC')


def profile_page(request):
    

    return render(request, 'scoop/profile_home.html')


def add_menu_item(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print form.errors
    else:
        form = ItemForm
    return render_to_response('scoop/add_menu_item.html', {'form': form}, context)


def index(request):

    return render(request, 'scoop/index.html')


def about(request):

    return render(request, 'scoop/about.html')


def reg_log(request):

    return render(request, 'scoop/reg_log.html')


def scan(request):
    if request.method == "POST":
        url = "http://api.v3.factual.com/t/products-cpg-nutrition?q=" + request.POST["scan"]
        print url
    return render(request, 'scoop/scan.html')


def register(request):
    if request.method == "POST":
        User.objects.create_user(request.POST["username"], None, request.POST["password"])
    return render(request, 'scoop/register.html')


def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST["username"],
                                 password=request.POST["password"])
        if user is not None:
            #the password verified for the user.
            if user.is_active:
                print ("User is valid, active and authenticated")
                return redirect('/add_menu_item.html')
            else:
                print ("This account has been DEACTIVATED.  Please contact Lunch Ladle customer service")

        else: # the authentication system was unable to verify the username and password
            print("The username and/or password were incorrect.")
    return render(request, 'scoop/login.html')


# def index(request):
#     context = RequestContext(request)
#     context_dict = {}
#     foods = list(Item.objects.all())
#     food_list = []
#     for f in foods:
#         food_list.append({
#             "name": f.item_name
#         })
#
#     return render_to_response('scoop/index.html', context_dict, context)


@csrf_exempt
def ajax(request):
    if request.method == "POST":
        item = Item()
        item.item_name = request.POST["item_name"]
        item.save()

    items = list(Item.objects.all())
    ajax_data = []
    for p in items:
        item_ingredients = []
        for i in p.ingredients.all():
            item_ingredients.append(i.ingredients)
        ajax_data.append({
            "item_category": p.item_category,
            "item_name": p.item_name,
            "item_ingredients": item_ingredients,
        })

    return HttpResponse(dumps(ajax_data), content_type="application/json")


def dom(request):
    if request.method == "POST":
        print request.POST

    return render(request, 'scoop/dom.html')

# from django.shortcuts import render, render_to_response
# from json import dumps, loads
# from models import Purchase, Item, Ingredient
# from django.http import HttpResponse
# from django.contrib.auth.models import User
# from django.contrib import auth
# from django.shortcuts import redirect
# from django.template import RequestContext, loader
# from django.views.decorators.csrf import csrf_exempt
# from factual import Factual
# from django.views.decorators.csrf import csrf_exempt
# import urllib
# import requests
# import json
#
# factual = Factual('2ReKJ6iWVlbUs0B10VixjPGSMw1uLW5UQtL7tJgC', 'Xb0cE0OFsGp8zmGENU7j8T2hzoaNH9cpYvj80WKC')
#
#
# @csrf_exempt
# def scan(request):
#     if request.method == "POST":
#         upc = request.POST["scan"]
#         data = {"KEY": "2ReKJ6iWVlbUs0B10VixjPGSMw1uLW5UQtL7tJgC", "q": upc}
#         params = urllib.urlencode(data)
#         url = ("http://api.v3.factual.com/t/products-cpg-nutrition?select=product_name,%20ingredients&" +
#                params)
#         f = urllib.urlopen(url)
#         # print (f.read())
#         j = f.read()
#         json_response = json.loads(j)
#         print json_response
#         product = json_response["response"]["data"][0]
#         product_print = product["product_name"]
#         ingredients = product["ingredients"]
#         for ingredient in ingredients:
#             print ingredient
#             context = RequestContext(request)
#             context_dict = {'product_name': product_print, 'product_code': upc}
#             return render_to_response('vendor/scan.html', context_dict, context)
#
#     return render(request, 'vendor/scan.html')
#
#
# @csrf_exempt
# def ajax(request):
#     if request.method == "POST":
#
#         item = Item()
#         item.item_code = request.POST["item_code"]
#         item.save()
#
#     items = list(Item.objects.all())
#     ajax_data = []
#     for p in items:
#         ingredients = []
#         for i in p.ingredients.all():
#             ingredients.append(i.ingredients)
#         ajax_data.append({
#             "scan": p.item_code,
#             "item_name": p.item_name,
#             "item_ingredients": ingredients,
#         })
#
#     return HttpResponse(dumps(ajax_data), content_type="application/json")
#
#
# def dom(request):
#     if request.method == "POST":
#         print request.POST
#
#     return render(request, 'vendor/scan.html')