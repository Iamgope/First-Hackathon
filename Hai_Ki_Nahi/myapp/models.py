from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
class Item(models.Model):
    tags = [('choice1','Books'),('choice2','Instruments'),('choice3','Bikes'),('choice4','Clothes'),]
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=300)
    item_img = models.ImageField(upload_to='images/')
    Tag = models.CharField(max_length=100,choices=tags)

    def __str__(self):
        return self.item_name

class UserDetail(models.Model):
    lended = models.OneToOneField(to=Item, on_delete=models.CASCADE)
    phone =  models.PositiveIntegerField()
