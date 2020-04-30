from rest_framework import serializers

from api.models import Company, Vacancy


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address',)


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'salary', 'company', )

    def to_representation(self, instance):
        self.fields['company'] = CompanySerializer(read_only=True)
        return super(VacancySerializer, self).to_representation(instance)


class CompanySerializer2(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        category = Company.objects.create(name=validated_data.get('name'),
                                          description=validated_data.get('description'),
                                          city=validated_data.get('city'),
                                          address=validated_data.get('address'))
        return category

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     return instance