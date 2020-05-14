from django.shortcuts import render, get_object_or_404
from .models import BlogList

def blog(request):
    bloglist = BlogList.objects.all()
    
    context = {
        "bloglist" : bloglist
    }
    return render(request, "blog/blog.html", context)

def single_blog(request, bloglist_id):
    
    blo = get_object_or_404(BlogList, pk=bloglist_id)
    context = {
        "blo" : blo
    }
    return render(request, "blog/single_blog.html", context)
