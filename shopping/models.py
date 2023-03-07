from django.db import models
from products.models import Product
from accounts.models import User


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qty = models.TextField()



class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qty = models.TextField()
    address = models.TextField()
    mobile = models.CharField(max_length=255)
    price= models.FloatField()
    discount = models.FloatField()
    date = models.DateField()
    status = models.CharField(max_length=255, 
                              choices=[
                                ('Requested','Requested'),
                                ('Dispatched','Dispatched'),
                                ('Delivered','Delivered'),
                                ('Cancelled','Cancelled'),
                                    ], default= ' Requested')



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='reviews', null=True, blank=True)
    rating = models.IntegerField()



