from django.shortcuts import render, render_to_response
from django import forms
from django_select2 import widgets
from json import dumps, loads
from models import Purchase, Item, Ingredient, ChildProfile
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django.template import RequestContext, loader
from django.db.models import Q
from django_select2 import Select2View, NO_ERR_RESP
from django.views.decorators.csrf import csrf_exempt
import urllib
import requests
import json
from factual import Factual
factual = Factual('2ReKJ6iWVlbUs0B10VixjPGSMw1uLW5UQtL7tJgC', 'Xb0cE0OFsGp8zmGENU7j8T2hzoaNH9cpYvj80WKC')


def about(request):
    return render(request, 'scoop/home_templates/about.html')


def add_menu_item(request):
    context = RequestContext(request)
    if request.method == 'GET' and 'stock_item' in request.GET:
        upc = request.GET["scan"]
        data = {"KEY": "2ReKJ6iWVlbUs0B10VixjPGSMw1uLW5UQtL7tJgC", "q": upc}
        params = urllib.urlencode(data)
        url = ("http://api.v3.factual.com/t/products-cpg-nutrition?select=brand,%20manufacturer,%20product_name,%20upc,\
                %20category,%20ingredients&" + params)
        f = urllib.urlopen(url)
        # print (f.read())
        j = f.read()
        json_response = json.loads(j)
        print json_response
        product = json_response["response"]["data"][0]
        brand = product["brand"]
        manufacturer = product["manufacturer"]
        product_name = product["product_name"]
        item_code = product["upc"]
        item_category = product["category"]
        ingredients = product["ingredients"]
        context = RequestContext(request)
        context_dict = {'brand': brand, 'manufacturer': manufacturer, 'product_name': product_name, 'item_code': item_code, 'item_category': item_category, 'ingredients': ingredients}
        return render_to_response('scoop/vendor_templates/add_menu_item.html', context_dict, context)
    elif request.method == 'POST':
        print request.POST
        ingredient_count = int(request.POST["ingredient_count"])
        item = Item()
        item.brand = request.POST["brand"]
        item.manufacturer = request.POST["manufacturer"]
        item.product_name = request.POST["product_name"]
        item.item_code = request.POST["item_code"]
        item.item_category = request.POST["item_category"]
        # item.ingredients = request.POST["ingredients"]
        item.save()
        for i in range(ingredient_count):
            input_name = "ingredient" + str(i+1)
            input_value = request.POST[input_name]
            results = Ingredient.objects.filter(ingredient=input_value)
            if len(results) == 0:
                ingredient = Ingredient()
                ingredient.ingredient = input_value
                ingredient.save()
            else:
                ingredient = results[0]

            item.ingredient.add(ingredient)

        return render(request, 'scoop/vendor_templates/add_menu_item.html')
    return render(request, 'scoop/vendor_templates/add_menu_item.html')
    #     form = ItemForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=True)
    #         return add_menu_item(context)
    #     else:
    #         print form.errors
    #     return render_to_response('scoop/add_menu_item.html', {'form': form}, context)
    # else:
    #     form = ItemForm
    # return render_to_response('scoop/add_menu_item.html', {'form': form}, context)


def cutting_board(request):
    context = RequestContext(request)
    ingredients = Ingredient.objects.all()
    child = ChildProfile()
    context_dict = {'ingredients': ingredients}
    if request.method == "POST":
        child.banned = request.POST["banned"]
        child.banned.add()
        return render_to_response('scoop/user_templates/cutting_board.html', context_dict, context)

    return render_to_response('scoop/user_templates/cutting_board.html', context_dict, context)


# class CuttingBoardSelect2View(Select2View):
#     def get_results(self, request, term, page, context):
#         ingredients = Ingredient.objects.filter(Q(ingredient__icontains=term))
#         res = [ingredient.ingredient for ingredient in ingredients]
#         return NO_ERR_RESP, False, res  # Any error response, Has more results, options list


def dom(request):
    if request.method == "POST":
        print request.POST
    return render(request, 'scoop/dom.html')


def index(request):
    return render(request, 'scoop/home_templates/index.html')


def login(request):
    # context = RequestContext(request)
    # if request.method == "Post":
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         return redirect(request, 'scoop/profile_home.html')
    context = RequestContext(request)
    if request.method == "POST":
        user = auth.authenticate(username=request.POST["username"],
                                 password=request.POST["password"])
        if user is not None:
            #the password verified for the user.
            if user.is_active:
                auth.login(request, user)
                print "User is valid, active and authenticated"
                return redirect('profile_home.html')
            else:
                error = "This account has been DEACTIVATED.  Please contact Lunch Ladle customer service"
                return render_to_response('scoop/home_templates/login.html', {"error": error}, context)
        else:  # the authentication system was unable to verify the username and password
            error = "The username and/or password were incorrect."
            return render_to_response('scoop/home_templates/login.html', {"error": error}, context)
    return render(request, 'scoop/home_templates/login.html')
    # form = LoginForm
    # return render_to_response('scoop/login.html', {"form": form}, context)


def logout(request):
    RequestContext(request)
    if auth.user_logged_in:
        auth.logout(request)
    return render(request, 'scoop/home_templates/logout.html')


def profile_home(request):
    return render(request, 'scoop/user_templates/profile_home.html')


def reg_log(request):
    return render(request, 'scoop/reg_log.html')


def register(request):
    if request.method == "POST":
        User.objects.create_user(request.POST["username"], None, request.POST["password"])
        return redirect('login.html')
    return render(request, 'scoop/home_templates/register.html')



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


# @csrf_exempt
# def ajax(request):
#     if request.method == "POST":
#         item = Item()
#         item.item_name = request.POST["item_name"]
#         item.save()
    #
    # items = list(Item.objects.all())
    # ajax_data = []
    # for p in items:
    #     item_ingredients = []
    #     for i in p.ingredients.all():
    #         item_ingredients.append(i.ingredients)
    #     ajax_data.append({
    #         "item_category": p.item_category,
    #         "item_name": p.item_name,
    #         "item_ingredients": item_ingredients,
    #     })

    # return HttpResponse(dumps(ajax_data), content_type="application/json")





def scan(request):
    if request.method == "POST":
        url = "http://api.v3.factual.com/t/products-cpg-nutrition?q=" + request.POST["scan"]
        print url
    return render(request, 'scoop/scan.html')

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
#     if request.method == "GET":
#         upc = request.GET["scan"]
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
#             return render_to_response('scoop/scan.html', context_dict, context)
#
#     return render(request, 'scoop/scan.html')
#
#
@csrf_exempt
def ajax(request):
    if request.method == "GET":

        item = Item()
        # item.item_code = request.GET["item_code"]
        # item.save()

    items = list(Item.objects.all())
    ajax_data = []
    for p in items:
        ingredients = []
        for i in p.ingredients.all():
            ingredients.append(i)
    ajax_data.append({
        "scan": p.item_code,
        "item_name": p.item_name,
        "item_ingredients": ingredients,
    })

    return HttpResponse(dumps(ajax_data), content_type="application/json")
#
#
# def dom(request):
#     if request.method == "POST":
#         print request.POST
#
#     return render(request, 'vendor/scan.html')