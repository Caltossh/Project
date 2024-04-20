from django.db import models
    
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()

    def to_json(self):
        return{
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price
        }

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

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
