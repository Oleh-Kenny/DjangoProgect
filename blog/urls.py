from django.urls import path

from . import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('<int:bloglist_id>', views.single_blog, name='single_blog')
   
]


