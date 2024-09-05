from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    number_plate = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f"{self.name} - {self.number_plate}"

    
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name
    
class CategoryData(models.Model):
    name = models.CharField(max_length=200)
    no_available = models.IntegerField()
    address = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    image = models.ImageField()
    cost_per_minute = models.IntegerField(validators=[MinValueValidator(0)])
    
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_data')
    
    def __str__(self) -> str:
        return f"{self.name} - {self.cost_per_minute}"