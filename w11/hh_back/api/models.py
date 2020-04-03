from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=100)
    address = models.TextField()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


def str1(company):
    return company.name


class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='vacancies')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'salary': self.salary,
            'company': str1(self.company)
        }