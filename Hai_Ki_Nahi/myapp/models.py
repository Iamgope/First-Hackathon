from django.db import models
from .models import User
# Create your models here.
class Item(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=300)
    item_img = models.ImageField()

    def __str__(self):
        return self.item_name
