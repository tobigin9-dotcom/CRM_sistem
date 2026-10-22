from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    name = models.CharField("название", max_length=200, unique=True)
    description = models.TextField("описание", blank=True)
    cost = models.DecimalField(
        "стоимость", max_digits=12, decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    class Meta:
        verbose_name = "услуга"
        verbose_name_plural = "услуги"
        ordering = ["name"]

    def __str__(self):
        return self.name
