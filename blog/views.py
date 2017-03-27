#coding=UTF-8
from django.shortcuts import render_to_response
from mysite.blog.models import BlogPost

def blogs(request):
    posts = BlogPost.objects.all()
    return render_to_response("blogs.html",{"posts":posts})

def search(request):
    keyword = request.GET['keyword']
    major = request.GET['major']
    print  "keyword="+keyword
    print 'major=:'+major
    allBlog = BlogPost.objects.all()
    SearchResult = []
    if keyword:
        print "keyword is %s"+keyword
        for x in allBlog:
            if keyword in x.title:
                if major == u'所有 ' or major == x.major:
                    SearchResult.append(x)
        return render_to_response("blogs.html",{"posts":SearchResult})
    else:
        print "no keyword"
        if major == u'所有':
            return render_to_response("blogs.html",{"posts":allBlog})
        else:
            for x in allBlog:
                if major == x.major:
                    SearchResult.append(x)
            return render_to_response("blogs.html",{"posts":SearchResult})        
# Create your views here.
