from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [("contracts", "0001_initial"), ("leads", "0001_initial")]
    operations = [migrations.CreateModel(
        name="Customer",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("contract", models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name="customer", to="contracts.contract", verbose_name="контракт")),
            ("lead", models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name="customer", to="leads.lead", verbose_name="потенциальный клиент")),
        ],
        options={"verbose_name": "активный клиент", "verbose_name_plural": "активные клиенты", "ordering": ["lead__last_name", "lead__first_name"]},
    )]
