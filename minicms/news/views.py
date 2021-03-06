# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Column, Article

# def index(request):
# 	response = "<h1>Welcome home!!! Grandpa An!!!</h1>"
# 	return HttpResponse(response)

def index(request):
	home_display_columns = Column.objects.filter(home_display=True)
	nav_display_columns = Column.objects.filter(nav_display=True)
	columns = Column.objects.all()
	return render(request, 'index.html', 
			{
				'nav_display_columns': nav_display_columns,
				# 'home_display_columns': home_display_columns, 
			},
		)

def column_detail(request, column_slug):
	column = Column.objects.get(slug=column_slug)
	return render(request, 'news/column.html', {'column': column})

def article_detail(request, pk, article_slug):
	article = Article.objects.get(pk = pk)
	if article_slug != article.slug:
		return redirect(article, permanent=True)
	return render(request, 'news/article.html', {'article': article})

    # article = Article.objects.filter(slug=article_slug)[0]
    # return render(request, 'news/article.html', {'article': article})
# Create your views here.
