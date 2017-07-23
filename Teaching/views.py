from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render

def Teaching(request):
    return render(request, 'teaching.html')

