from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from api.models import Company, Vacancy


def companies_list(request):
    companies = Company.objects.all()
    j_c = [c.to_json() for c in companies]
    return JsonResponse(j_c, safe=False)


def one_comp(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return HttpResponse(f'<h2>{e}</h2>')
    return JsonResponse(company.to_json(), safe=False)


def vac_by_comp(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return HttpResponse(f'<h2>{e}</h2>')

    vacancies = company.vacancies.all()
    j_v = [v.to_json() for v in vacancies]
    return JsonResponse(j_v, safe=False)


def vac_list(request):
    vac = Vacancy.objects.all()
    j_v = [v.to_json() for v in vac]
    return JsonResponse(j_v, safe=False)


def one_vac(request):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Company.DoesNotExist as e:
        return HttpResponse(f'<h2>{e}</h2>')
    return JsonResponse(vacancy.to_json())


def top_ten(request):
    vacancies = Vacancy.objects.order_by('-salary')
    j_v = [v.to_json() for v in vacancies]
    return JsonResponse(j_v[:10], safe=False)