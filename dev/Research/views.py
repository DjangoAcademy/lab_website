from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render

def Research(request):
    return render(request, 'research.html')

