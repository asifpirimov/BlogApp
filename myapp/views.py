from django.shortcuts import render
from django.http.response import HttpResponse
from myapp.models import MyApp
from myapp.models import Category
# Create your views here.



def index(request):
    context = {
         "blogs": MyApp.objects.filter(is_active = True),
         "categories": Category.objects.all()
    }
    return render(request, "myapp/index.html", context)

def blogs(request):
        context = {
         "blogs": MyApp.objects.filter(is_active = True),
         "categories": Category.objects.all()
    }
        return render(request, "myapp/blogs.html", context)

def blog_details(request, slug):
    blog = MyApp.objects.get(slug=slug)
    return render(request, "myapp/blog-details.html", {"blog": blog})

def blogs_by_category(request, slug):
        context = {
        "blogs": Category.objects.get(slug = slug).myapp_set.filter(is_active = True),
         #"blogs": MyApp.objects.filter(is_active = True, category__slug = slug),
         "categories": Category.objects.all(),
         "selected_category": slug,
    }
        return render(request, "myapp/blogs.html", context)


      