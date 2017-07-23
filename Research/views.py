from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render

def Research(request):
    context = {'slr' : 'this is dummy text in research.views'}
    return render(request, 'research.html', context)
