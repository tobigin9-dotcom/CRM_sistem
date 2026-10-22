from django.core.validators import MinValueValidator
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [("products", "0001_initial")]
    operations = [migrations.CreateModel(
        name="Advertisement",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=200, unique=True, verbose_name="название")),
            ("channel", models.CharField(max_length=100, verbose_name="канал продвижения")),
            ("budget", models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(0)], verbose_name="бюджет")),
            ("product", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="advertisements", to="products.product", verbose_name="услуга")),
        ],
        options={"verbose_name": "рекламная кампания", "verbose_name_plural": "рекламные кампании", "ordering": ["name"]},
    )]
