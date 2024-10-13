from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FoodEntry(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  food_item = models.CharField(max_length = 100)
  calories = models.IntegerField()
  meal_choices=[
    ('Breakfast', 'Breakfast'), 
    ('Lunch', 'Lunch'), 
    ('Supper', 'Supper')]
  meal_type = models.CharField(max_length = 10, choices= meal_choices)

  def __str__(self):
    return f'{self.user} - {self.calories} calories'
  
