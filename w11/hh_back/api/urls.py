from django.urls import path

from api.views import companies_list, one_comp, vac_by_comp, vac_list, one_vac, top_ten

urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:id>/', one_comp),
    path('companies/<int:id>/vacancies/', vac_by_comp),
    path('vacancies/', vac_list),
    path('vacancies/<int:id>/', one_vac),
    path('vacancies/top_ten/', top_ten)
]