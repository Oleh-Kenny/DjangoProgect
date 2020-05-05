from django.contrib import admin

from .models import CarManager

class CarManagersAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "phone_1", "phone_2", "telegram", "emaile", "is_published")
    list_display_links = ("name", "phone", "emaile", "phone_1", "phone_2", "telegram")
    list_editable = ("is_published",)
    search_fields = ("name", "phone", "emaile", "rating")
    list_filter = ("name",)
    list_per_page = 25
    
admin.site.register(CarManager, CarManagersAdmin)
