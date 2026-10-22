from django.core.validators import MinValueValidator
from django.db import models


class Contract(models.Model):
    name = models.CharField("название", max_length=200)
    product = models.ForeignKey(
        "products.Product", verbose_name="услуга",
        on_delete=models.PROTECT, related_name="contracts",
    )
    document = models.FileField("файл договора", upload_to="contracts/%Y/%m/", blank=True)
    start_date = models.DateField("начало действия")
    end_date = models.DateField("окончание действия")
    cost = models.DecimalField(
        "сумма договора", max_digits=12, decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    class Meta:
        verbose_name = "контракт"
        verbose_name_plural = "контракты"
        ordering = ["-start_date", "name"]

    def __str__(self):
        return self.name
