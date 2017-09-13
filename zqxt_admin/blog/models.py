# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# from django.utils.encoding import python_2_unicode_compatible

# @python_2_unicode_compatible
class Article(models.Model):
	title = models.CharField(u'标题', max_length=256)
	content = models.TextField(u'内容')

	pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
	update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)
	
	def __unicode__(self):
		return self.title

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def my_property(self):
        return self.first_name + ' ' + self.last_name
    my_property.short_description = "Full name of the person"
 
    full_name = property(my_property)

class PersonAdmin(admin.ModelAdmin):
	list_display = ('name', 'age')
	search_fields = ('name',)

	def get_search_results(self, request, queryset, search_term):
		queryset, use_distinct = super(PersonAdmin, self).get_search_results(request, queryset, search_term)
		try:
			search_term_as_int = int(search_term)
			queryset |= self.model.objects.filter(age=search_term_as_int)
		except Exception as e:
			pass
		return queryset, use_distinct

class ArticleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if change:# 更改的时候
            obj_original = self.model.objects.get(pk=obj.pk)
        else:# 新增的时候
            obj_original = None
 
        obj.user = request.user
        obj.save()
# Create your models here.
