from django.shortcuts import render
from .models import Blog,Category

# Create your views here.

def home(request):
    blogs  = Blog.objects.all()
    category = Category.objects.all()
    return render(request,'index.html',{'blogs':blogs})
def blog_content(request,id):
    blog = Blog.objects.get(id=id)
    return render (request,'content.html',{'blog':blog})

def blog_form(request):
    if request.method =="POST":
        print(request.POST)
    else:
        pass
    return render(request,'blog_form.html')