from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    category_id = models.IntegerField()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'category_id': self.category_id
        }


class Category(models.Model):
    name = models.CharField(max_length=1)

    def to_json(self):
        return {
            'category_id': self.id,
            'name': self.name
        }
