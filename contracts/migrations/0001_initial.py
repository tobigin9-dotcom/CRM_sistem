from django.core.validators import MinValueValidator
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [("products", "0001_initial")]
    operations = [migrations.CreateModel(
        name="Contract",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=200, verbose_name="название")),
            ("document", models.FileField(blank=True, upload_to="contracts/%Y/%m/", verbose_name="файл договора")),
            ("start_date", models.DateField(verbose_name="начало действия")),
            ("end_date", models.DateField(verbose_name="окончание действия")),
            ("cost", models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(0)], verbose_name="сумма договора")),
            ("product", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="contracts", to="products.product", verbose_name="услуга")),
        ],
        options={"verbose_name": "контракт", "verbose_name_plural": "контракты", "ordering": ["-start_date", "name"]},
    )]
