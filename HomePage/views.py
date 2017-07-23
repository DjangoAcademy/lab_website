from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from BH_LAB.settings import STATICFILES_DIRS
import os
import os.path as op

def HomePage(request):
    # template directory must be on path in settings.py
    carousel_images = os.listdir(op.join(STATICFILES_DIRS[0], 'Images', 'home'))
    context = {'carousel_image_list' : carousel_images}
    return render(request, 'homepage.html', context)
