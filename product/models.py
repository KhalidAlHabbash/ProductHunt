from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    product_image = models.ImageField(upload_to="images/")
    product_desc = models.TextField(blank=True)
    product_title = models.CharField(max_length=200)
    product_date = models.DateField()
    product_icon = models.ImageField(upload_to="images/")
    product_url =  models.TextField()
    product_votes = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return (self.product_title)

