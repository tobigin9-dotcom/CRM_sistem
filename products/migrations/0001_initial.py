from django.core.validators import MinValueValidator
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [migrations.CreateModel(
        name="Product",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=200, unique=True, verbose_name="название")),
            ("description", models.TextField(blank=True, verbose_name="описание")),
            ("cost", models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(0)], verbose_name="стоимость")),
        ],
        options={"verbose_name": "услуга", "verbose_name_plural": "услуги", "ordering": ["name"]},
    )]
