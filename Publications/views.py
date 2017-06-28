from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render

def Publications(request):
    return render(request, 'publications.html')

