from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [("advertisements", "0001_initial")]
    operations = [migrations.CreateModel(
        name="Lead",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("first_name", models.CharField(max_length=100, verbose_name="имя")),
            ("last_name", models.CharField(max_length=100, verbose_name="фамилия")),
            ("phone", models.CharField(max_length=30, verbose_name="телефон")),
            ("email", models.EmailField(max_length=254, verbose_name="email")),
            ("advertisement", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="leads", to="advertisements.advertisement", verbose_name="рекламная кампания")),
        ],
        options={"verbose_name": "потенциальный клиент", "verbose_name_plural": "потенциальные клиенты", "ordering": ["last_name", "first_name"]},
    )]
