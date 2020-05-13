from django.contrib import admin

from .models import BlogList

class BlogListAdmin(admin.ModelAdmin):
    list_display = ("name_list", "blog_date", "text_list", "carmanager", "rating")
    list_display_links = ("name_list", "blog_date", "text_list", "carmanager", "rating")
    search_fields = ("name_list", "blog_date", "text_list", "carmanager", "rating")
    list_per_page = 20

admin.site.register(BlogList, BlogListAdmin)
