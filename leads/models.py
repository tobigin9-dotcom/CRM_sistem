from django.core.validators import RegexValidator
from django.db import models


class Lead(models.Model):
    first_name = models.CharField("имя", max_length=100)
    last_name = models.CharField("фамилия", max_length=100)
    phone = models.CharField(
        "телефон",
        max_length=30,
        validators=[
            RegexValidator(
                regex=r"^\+?(?=(?:\D*\d){7,15}\D*$)[0-9\s().-]+$",
                message=(
                    "Введите корректный номер телефона: "
                    "от 7 до 15 цифр."
                ),
            )
        ],
    )
    email = models.EmailField("email")
    advertisement = models.ForeignKey(
        "advertisements.Advertisement",
        verbose_name="рекламная кампания",
        on_delete=models.PROTECT,
        related_name="leads",
    )

    class Meta:
        verbose_name = "потенциальный клиент"
        verbose_name_plural = "потенциальные клиенты"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
