from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from api.models import Company, Vacancy
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import CompanySerializer, CompanySerializer2


@api_view(['GET', 'POST'])
def companies_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer2(companies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CompanySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE', ])
def one_comp(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return HttpResponse(f'<h2>{e}</h2>')

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        company.delete()
        return Response({'deleted': True})


def vac_by_comp(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return HttpResponse(f'<h2>{e}</h2>')

    vacancies = company.vacancies.all()
    j_v = [v.to_json() for v in vacancies]
    return JsonResponse(j_v, safe=False)


def top_ten(request):
    vacancies = Vacancy.objects.order_by('-salary')
    j_v = [v.to_json() for v in vacancies]
    return JsonResponse(j_v[:10], safe=False)