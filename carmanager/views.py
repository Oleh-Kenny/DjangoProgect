from django.shortcuts import render

# from .models import CarManager
# from django.core.paginator import Paginator

# def index(request):
#     carmanager = CarManager.objects.all().filter(is_pablished=True)

#     paginator = Paginator(carmanager, 6)
#     page = request.GET.get("page")
#     paged_carmanager = paginator.get_page(page)

#     context = {
#         "carmanager" : paged_carmanager,
#         "title" : "About Us"
#     }
#     return render(request, "pages/about.html", context)