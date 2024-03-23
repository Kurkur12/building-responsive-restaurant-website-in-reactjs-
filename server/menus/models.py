from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Categories'


class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='images/')
    price = models.FloatField()
    description = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name_plural = 'Menus'
