from django.db import models
from django.contrib.auth.models import User
# Create your models here.
MODEL_CHOICES = [
    ('iPhone 6', 'iPhone 6'),
    ('iPhone 6 Plus', 'iPhone 6 Plus'),
    ('iPhone 6S', 'iPhone 6S'),
    ('iPhone 6S Plus', 'iPhone 6S Plus'),
    ('iPhone 7', 'iPhone 7'),
    ('iPhone 7 Plus', 'iPhone 7 Plus'),
    ('iPhone 8', 'iPhone 8'),
    ('iPhone 8 Plus', 'iPhone 8 Plus'),
    ('iPhone X', 'iPhone X'),
    ('iPhone XR', 'iPhone XR'),
    ('iPhone XS', 'iPhone XS'),
    ('iPhone XS Max', 'iPhone XS Max'),
    ('iPhone 11', 'iPhone 11'),
    ('iPhone 11 Pro', 'iPhone 11 Pro'),
    ('iPhone 11 Pro Max', 'iPhone 11 Pro Max'),
    ('iPhone 12', 'iPhone 12'),
    ('iPhone 12 Mini', 'iPhone 12 Mini'),
    ('iPhone 12 Pro', 'iPhone 12 Pro'),
    ('iPhone 12 Pro Max', 'iPhone 12 Pro Max'),
    ('iPhone 13', 'iPhone 13'),
    ('iPhone 13 Mini', 'iPhone 13 Mini'),
    ('iPhone 13 Pro', 'iPhone 13 Pro'),
    ('iPhone 13 Pro Max', 'iPhone 13 Pro Max'),
    ('iPhone 14', 'iPhone 14'),
    ('iPhone 14 Plus', 'iPhone 14 Plus'),
    ('iPhone 14 Pro', 'iPhone 14 Pro'),
    ('iPhone 14 Pro Max', 'iPhone 14 Pro Max'),
    ('iPhone 15', 'iPhone 15'),
    ('iPhone 15 Plus', 'iPhone 15 Plus'),
    ('iPhone 15 Pro', 'iPhone 15 Pro'),
    ('iPhone 15 Pro Max', 'iPhone 15 Pro Max'),
    ('iPhone 16', 'iPhone 16'),
    ('iPhone 16+', 'iPhone 16+'),
]
class Cover(models.Model):
    phone=models.CharField(choices=MODEL_CHOICES,default='iphone 16',max_length=25)
    price=models.IntegerField(default=9.99)
    desc=models.TextField(max_length=100)
    photo=models.ImageField()



class Orders(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    phone=models.CharField(choices=MODEL_CHOICES,default='iphone 16',max_length=25)
    price=models.IntegerField(default=10)
    address=models.TextField(max_length=500,default='canada')
    postalcode=models.TextField(max_length=7,default='000000')
    paymenttype=models.TextField(default="Cash on delivery")
