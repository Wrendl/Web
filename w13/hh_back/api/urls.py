from django.urls import path

from api.views.views import *
from api.views.views1 import CompanyListAPIView
from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework_jwt.views import obtain_jwt_token
from api.views.views1 import *
from api.views.views2 import *

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', companies_list),
    path('companies/<int:id>/', one_comp),
    path('companies/<int:id>/vacancies/', vac_by_comp),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:id>/', VacancyDetailAPIView.as_view()),
    path('vacancies/top_ten/', top_ten)
]