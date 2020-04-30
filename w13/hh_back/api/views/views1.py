from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.models import Company

from api.serializers import CompanySerializer


class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    #permission_classes = (IsAuthenticated,)