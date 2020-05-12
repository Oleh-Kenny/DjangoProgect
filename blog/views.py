from django.shortcuts import render

def blog(request):
    return render(request, "blog/blog.html")

def single_blog(request):
    return render(request, "blog/single_blog.html")
