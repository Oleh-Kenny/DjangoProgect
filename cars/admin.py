from django.contrib import admin

from .models import CarsList


class CarListAdmin(admin.ModelAdmin):
    list_display = ("id", "vendor", "model", "engine",
                    "color", "price", "rating", "carmanager_id", "is_published")  # показує в адмін панелі рядкі
    # робить клікабельним вибрані рядкі
    list_display_links = ("id", "vendor", "model")
    # дає мождивість ставить відмітки в паблішид
    list_editable = ("is_published",)
    search_fields = ("vendor", "price", "model", "engine",
                     "rating")  # пошук по вибраним категоріям
    list_per_page = 25  # пагінація
    list_filter = ("carmanager_id", "vendor")


admin.site.register(CarsList, CarListAdmin)
