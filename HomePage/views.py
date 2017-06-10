from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render

def HomePage(request):
    # return HttpResponse(render, 'index_dummy.html')
    # template directory must be on path in settings.py
    return render(request, 'home.html')

def _nav(request):
    return render(request, '_nav.html')

def BasePage(request):
    return render(request, '__base.html')

def ODUHead(request):
    return render(request, 'ODU_head.html')

def Adams(request):
    return render(request, 'sebs-adams.html')

def Home(request):
    return render(request, 'index.html')

def Garage(request):
    return render(request, 'index-orig.html')
