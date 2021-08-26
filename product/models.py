from django.db import models
from django.contrib.auth.models import User

# Product Model
class Product(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    user_phone = models.IntegerField(default=None)
    prod_id = models.AutoField(primary_key=True, default=None)
    prod_cat = models.TextField(max_length=30, default=None)
    prod_title = models.TextField(max_length=50, default=None)
    prod_desc = models.CharField(max_length=200, default=None)
    prod_condition = models.TextField(max_length=4, default=None)
    prod_price = models.IntegerField(default=None)
    prod_location = models.TextField()
    prod_date = models.DateTimeField()
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    image4 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.prod_title

# Product Category Model
class Prod_Cat(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.TextField(max_length=30)
    cat_slug = models.TextField(max_length=20, default='')

    def __str__(self):
        return self.cat_name
