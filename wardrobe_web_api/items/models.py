from django.db import models
    
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def to_json(self):
        return{
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
    
    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
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
    
    def __str__(self) -> str:
        return self.name


class Photo(models.Model):
    id = models.IntegerField(primary_key=True)
    imageUrl = models.TextField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='photos')

    def to_json(self):
        return{
            "id": self.id,
            "image_url": self.image.url if self.image else None
        }
    
    def __str__(self):
        return f"Photo ID: {self.id}, Item: {self.item.name}"
    



