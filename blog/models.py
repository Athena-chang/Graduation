#coding=UTF-8
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# from django import  forms
# from django.template.defaultfilters import default


class BlogPost (models .Model  )  :
    professor = models.CharField(max_length = 20)
    title  =  models.CharField(max_length=150)
    intro =  models. TextField()
    major = models.CharField(max_length = 20)
    selected = models.BooleanField(default = False)
class  BlogPostAdmin(admin.ModelAdmin):
    list_display  =  (  'title', 'professor'  )




# class BlogFilter(forms.Form):
#     field = forms.ChoiceField(choices=FIELD_CHOISE)   
#     text =  forms.CharField(max_length=20)
admin.site.register(BlogPost,BlogPostAdmin)
