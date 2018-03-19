from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from geoposition.fields import GeopositionField

# class Category(models.Model):
#     c_name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.c_name
#
#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'

class Site(models.Model):
    CHOICES = (
        ('apartments','Apartments'),
        ('houses','Houses'),
        ('land','Land'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20,choices=CHOICES)
    #category = models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE)
    position = GeopositionField()
    descrip = models.TextField(max_length=300)
    cost = models.DecimalField(decimal_places=2,max_digits=20)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title
