from django.db import models

class ItemCategory(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name

class ItemSize(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.name

# Create your models here.
class ShopItem(models.Model):
    product_code = models.IntegerField()
    name = models.CharField(max_length=20)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    size = models.ForeignKey(ItemSize, on_delete=models.PROTECT)
    image = models.CharField(max_length=250)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name
