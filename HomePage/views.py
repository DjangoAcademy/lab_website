from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render

def HomePage(request):
    # return HttpResponse(render, 'index_dummy.html')
    # template directory must be on path in settings.py
    return render(request, 'home.html')

def BasePage(request):
    return render(request, 'base.html')

def ODUHead(request):
    return render(request, 'ODU_head.html')
