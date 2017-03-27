from django.conf.urls import url
from mysite.blog.views import blogs,search

urlpatterns =[
    url(r'^$',blogs),
    url(r'^search$',search),
]
