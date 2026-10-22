from django.db import models


class Customer(models.Model):
    lead = models.OneToOneField(
        "leads.Lead", verbose_name="потенциальный клиент",
        on_delete=models.PROTECT, related_name="customer",
    )
    contract = models.OneToOneField(
        "contracts.Contract", verbose_name="контракт",
        on_delete=models.PROTECT, related_name="customer",
    )

    class Meta:
        verbose_name = "активный клиент"
        verbose_name_plural = "активные клиенты"
        ordering = ["lead__last_name", "lead__first_name"]

    def __str__(self):
        return str(self.lead)
