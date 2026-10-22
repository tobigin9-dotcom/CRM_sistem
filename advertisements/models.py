from django.core.validators import MinValueValidator
from django.db import models


class Advertisement(models.Model):
    name = models.CharField("название", max_length=200, unique=True)
    product = models.ForeignKey(
        "products.Product", verbose_name="услуга",
        on_delete=models.PROTECT, related_name="advertisements",
    )
    channel = models.CharField("канал продвижения", max_length=100)
    budget = models.DecimalField(
        "бюджет", max_digits=12, decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    class Meta:
        verbose_name = "рекламная кампания"
        verbose_name_plural = "рекламные кампании"
        ordering = ["name"]

    def __str__(self):
        return self.name
