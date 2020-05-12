from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('contacts', views.contact, name="contacts"),
    path('search', views.search, name ="search"),
    path('singlecar', views.search, name ="singlecar"),
    path('blog', views.blog, name="blog")
   
    

]
