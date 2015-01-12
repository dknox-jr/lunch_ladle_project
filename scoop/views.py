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
factual = Factual('2ReKJ6iWVlbUs0B10VixjPGSMw1uLW5UQtL7tJgC', 'Xb0cE0OFsGp8zmGENU7j8T2hzoaNH9cpYvj80WKC')


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
                return redirect('list')
            else:
                print ("The password is valid, but the account has been disabled!")

        else: # the authentication system was unable to verify the username and password
            print("The username and password were incorrect.")
    return render(request, 'scoop/login.html')


def index(request):
    context = RequestContext(request)
    context_dict = {}
    foods = list(Item.objects.all())
    food_list = []
    for f in foods:
        food_list.append({
            "name": f.item_name
        })

    return render_to_response('scoop/index.html', context_dict, context)


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