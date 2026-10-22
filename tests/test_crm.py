from datetime import date, timedelta
from decimal import Decimal

import pytest
from django.urls import reverse

from advertisements.models import Advertisement
from contracts.models import Contract
from customers.models import Customer
from leads.models import Lead
from products.models import Product



@pytest.mark.django_db
def test_dashboard_counts(client, django_user_model):
    user = django_user_model.objects.create_superuser("admin", "admin@example.com", "password")
    product = Product.objects.create(name="SEO", cost=Decimal("1000.00"))
    ad = Advertisement.objects.create(name="Spring", product=product, channel="Social", budget=Decimal("100"))
    Lead.objects.create(first_name="Ivan", last_name="Ivanov", phone="123", email="ivan@example.com", advertisement=ad)
    client.force_login(user)
    response = client.get(reverse("dashboard"))
    assert response.status_code == 200
    assert response.context["products_count"] == 1
    assert response.context["advertisements_count"] == 1
    assert response.context["leads_count"] == 1
    assert response.context["customers_count"] == 0


@pytest.mark.django_db
def test_statistics_counts_revenue_and_ratio(client, django_user_model):
    user = django_user_model.objects.create_superuser("admin", "admin@example.com", "password")
    product = Product.objects.create(name="SEO", cost=Decimal("1000.00"))
    ad = Advertisement.objects.create(name="Spring", product=product, channel="Social", budget=Decimal("100"))
    lead_one = Lead.objects.create(first_name="Ivan", last_name="Ivanov", phone="1", email="ivan@example.com", advertisement=ad)
    lead_two = Lead.objects.create(first_name="Petr", last_name="Petrov", phone="2", email="petr@example.com", advertisement=ad)
    contract_one = Contract.objects.create(name="C-1", product=product, start_date=date.today(), end_date=date.today() + timedelta(days=30), cost=Decimal("300"))
    contract_two = Contract.objects.create(name="C-2", product=product, start_date=date.today(), end_date=date.today() + timedelta(days=60), cost=Decimal("200"))
    Customer.objects.create(lead=lead_one, contract=contract_one)
    Customer.objects.create(lead=lead_two, contract=contract_two)
    client.force_login(user)
    response = client.get(reverse("ad-statistic"))
    assert response.status_code == 200
    row = response.context["ads"][0]
    assert row.leads_count == 2
    assert row.customers_count == 2
    assert row.revenue == Decimal("500")
    assert row.profit == Decimal("5")


@pytest.mark.django_db
def test_customer_form_does_not_offer_already_converted_lead(client, django_user_model):
    user = django_user_model.objects.create_superuser("admin", "admin@example.com", "password")
    product = Product.objects.create(name="SEO", cost=Decimal("1000"))
    ad = Advertisement.objects.create(name="Spring", product=product, channel="Social", budget=Decimal("100"))
    lead = Lead.objects.create(first_name="Ivan", last_name="Ivanov", phone="1", email="ivan@example.com", advertisement=ad)
    contract = Contract.objects.create(name="C-1", product=product, start_date=date.today(), end_date=date.today() + timedelta(days=30), cost=Decimal("300"))
    Customer.objects.create(lead=lead, contract=contract)
    client.force_login(user)
    response = client.get(reverse("customer-create"))
    assert response.status_code == 200
    assert lead not in response.context["form"].fields["lead"].queryset


@pytest.mark.django_db
def test_user_without_permission_cannot_open_products(client, django_user_model):
    user = django_user_model.objects.create_user("regular", password="password")
    client.force_login(user)
    response = client.get(reverse("product-list"))
    assert response.status_code == 403
