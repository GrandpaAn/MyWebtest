"""minicms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from news import views
from tools import views
from DjangoUeditor import urls as DjangoUeditor_urls

urlpatterns = [
	# url(r'^$', views.index, name='index'),
	# url(r'^column/(?P<column_slug>[^/]+)/$', views.column_detail, name='column'),
	# url(r'^news/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$', views.article_detail, name='article'),
 
    url(r'^admin/', include(admin.site.urls)),  
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^qrcode/(.+)$', views.generate_qrcode, name='qrcode'),
]
