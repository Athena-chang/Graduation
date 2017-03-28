#coding=UTF-8
from django.shortcuts import render_to_response
from mysite.blog.models import BlogPost

def blogs(request):
    posts = BlogPost.objects.all()  
    return render_to_response("blogs.html",{"posts":posts})

def search(request):
    keyword = request.GET['keyword']
    major = request.GET['major']
    try :
        onlySelectable = request.GET["onlySelectable"]
    except:
        onlySelectable = False
    print "*"*30
    print request.GET
    print onlySelectable
    print "*"*30
    posts = BlogPost.objects.all()
    if  onlySelectable:
        print "&&&&&&&&&&&&&&&&&"
        posts = posts.filter(selected=False)
    SearchResult = []
    num = 0
#     def get_context_data(self, **kwargs):
#         context = super(search, self).get_context_data(**kwargs)
#         context['count'] ={"major":"jijjj"}
#         return context
    for post  in posts:
        if keyword:
            if keyword not in post.title:
                continue
            if major != u"所有" and major != post.major:
                continue
        else:
            if major:
                if major != u"所有" and major !=post.major:
                    continue
        num = num +1
        SearchResult.append(post)
    
    return render_to_response("search.html",{"posts":SearchResult,"major":major,"keyword":keyword,"num":num,"onlySelectable":onlySelectable})       
#     if keyword:
#         for x in allBlog:
#             if keyword in x.title:
#                 SearchResult.append(x)
#         return render_to_response("blogs.html",{"posts":SearchResult})
#     else:
#         return render_to_response("blogs.html",{"posts":allBlog})


#     if keyword:
#         print "keyword is %s"+keyword
#         for x in allBlog:
#             if keyword in x.title:
#                 if major == u'所有 ' or major == x.major:
#                     SearchResult.append(x)
#         return render_to_response("blogs.html",{"posts":SearchResult})
#     else:
#         print "no keyword"
#         if major == u'所有':
#             return render_to_response("blogs.html",{"posts":allBlog})
#         else:
#             for x in allBlog:
#                 if major == x.major:
#                     SearchResult.append(x)
#             return render_to_response("blogs.html",{"posts":SearchResult})        

