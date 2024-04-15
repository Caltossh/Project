from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def to_json(self):
        return{
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "season": self.season,
            "size": self.size,
            "amount": self.amount,
            "price": self.price,
            "description": self.description 
        }
