# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# def home(request):
# 	return render(request, 'home.html')

def home(request):
	string = u"Grandpa An used Django to build a web"
	return render(request, 'home.html', {'string': string})

def TutorialList(request):
	TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
	return render(request, 'home.html', {'TutorialList': TutorialList})

def info_dict(request):
	info_dict = {'site': u'Grandpa An', 'content': u'搞事情！搞事情！搞事情！搞事情！'}
	return render(request, 'home.html', {'info_dict': info_dict})

def List(request):
	List = map(str, range(1000))# 一个长度为1000的 List
	return render(request, 'home.html', {'List': List})

def athlete_list(request):
	athlete_list = ["liuxiang", "sunyang", "fudalao", "Grandpa An"]
	return render(request, 'home.html', {'athlete_list': athlete_list})

# def add(request, a, b):
#     c = int(a) + int(b)
#     return HttpResponse(str(c))
# Create your views here.
