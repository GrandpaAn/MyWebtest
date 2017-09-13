# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse(u"Welcome to Grandpa An's home!")

# Create your views here.
