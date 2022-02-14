
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from myblog.models import hakkimda, post
# Create your views here.
def anasayfa(request):
    contex = {
        "blog":hakkimda.objects.filter(onhome=True)  
    }
    return render(request, "blog/index.html", contex)

def hakkimda_detail(request,pk):
    post = hakkimda.objects.get(pk=pk) 
    return render(request, 'blog/detail.html', {'post': post})    

def hakkimda_post_list(request):
        contex = {
        "blog":hakkimda.objects.all()
        }
        return render(request, "blog/hakkimdalist.html", contex)
def blog_index(request):
    contex = {
        "posts" : post.objects.all()
    }
    return render(request,"blog/blog.html", contex)

def blog_detail(request,pk):
    posts = post.objects.get(pk=pk) 
    return render(request, 'blog/blogdetail.html', {'post': posts})        

 