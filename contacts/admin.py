from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'car', 'email', 'phone', 'contact_date')
    list_display_links = ("name", "email", 'car')
    search_filter = ('name', 'email', 'car')
    pagination = 25


admin.site.register(Contact, ContactAdmin)