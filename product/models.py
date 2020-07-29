from django.db import models

class Product(models.Model):
    product_image = models.ImageField(upload_to="images/")
    product_desc = models.TextField(blank=True)
    product_title = models.CharField(max_length=200)

