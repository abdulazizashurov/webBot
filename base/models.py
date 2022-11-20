from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=300)  # Burger
    price = models.FloatField()  # 3.99$
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return f"{self.name} - {self.price} $"
