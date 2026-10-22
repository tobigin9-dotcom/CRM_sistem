from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

FULL = ("add", "change", "view", "delete")
ROLES = {
    "Оператор": {"leads.lead": FULL},
    "Маркетолог": {
        "products.product": FULL,
        "advertisements.advertisement": FULL,
    },
    "Менеджер": {
        "contracts.contract": FULL,
        "leads.lead": ("view",),
        "customers.customer": FULL,
    },
}


class Command(BaseCommand):
    help = "Создаёт группы CRM и назначает им разрешения"

    def handle(self, *args, **options):
        for group_name, models in ROLES.items():
            group, _created = Group.objects.get_or_create(name=group_name)
            permissions = []
            for label, actions in models.items():
                app_label, model_name = label.split(".")
                codenames = [f"{action}_{model_name}" for action in actions]
                permissions.extend(Permission.objects.filter(
                    content_type__app_label=app_label,
                    content_type__model=model_name,
                    codename__in=codenames,
                ))
            group.permissions.set(permissions)
            self.stdout.write(self.style.SUCCESS(f"Роль «{group_name}» настроена"))
