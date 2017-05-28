from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render

def HomePage(request):
    # return HttpResponse(render, 'index_dummy.html')
    # template directory must be on path in settings.py
    return render(request, 'home_dummy.html')

def BasePage(request):
    return render(request, 'base_dummy.html')
