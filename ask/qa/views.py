#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
from qa.pages import pages, quest, ask, login, signup

def test(request, *args, **kwargs):
    return HttpResponse('OK')

