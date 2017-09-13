"""zqxt_tmpl URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from learn import views as learn_views

urlpatterns = [
	url(r'^$', learn_views.home, name='home'),
    url(r'^string/$', learn_views.TutorialList, name='TutorialList'),
    url(r'^info_dict/$', learn_views.info_dict, name='info_dict'),
    url(r'^List/$', learn_views.List, name='List'),
    url(r'^athlete_list/$', learn_views.athlete_list, name='athlete_list'),
    url(r'^admin/', include(admin.site.urls)),
]
