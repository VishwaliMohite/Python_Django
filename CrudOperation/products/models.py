from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    stock = models.PositiveIntegerField()
    # image = models.ImageField(blank=True)

    def __str__(self):
        return self.name