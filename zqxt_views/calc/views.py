# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def add(request):
	a = request.GET.get('a', 0)
	b = request.GET.get('b', 0)
	c = int(a) + int(b)
	return HttpResponse(str(c))

def add2(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))

def old_add2_redirect(request, a, b):
	return HttpResponseRedirect(
			reverse('add2', args=(a, b))
		)

# Create your views here.
