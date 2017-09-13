# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!!!  Goodbye World!!!'
    return render(request, 'hello.html', context)
# 	# return HttpResponse("Hello world!!!")

def home(result):
	athlete=["Grandpaan", "baidu", "tianmao", "xiaomi", "hhhhhhhh"]
	return render(result, 'base.html', {'athlete':athlete})

def home(request):
	TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
	return render(request, 'home.html', {'TutorialList': TutorialList})
	


# print "hello world"