from django.shortcuts import render, render_to_response
from json import dumps, loads
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from factual import Factual
factual = Factual('2ReKJ6iWVlbUs0B10VixjPGSMw1uLW5UQtL7tJgC', 'Xb0cE0OFsGp8zmGENU7j8T2hzoaNH9cpYvj80WKC')


def index(request):

    return render(request, 'll_home/index.html')


def about(request):

    return render(request, 'll_home/about.html')

def reg_log(request):

    return render(request, 'll_home/reg_log.html')