
from typing import Any

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create or update an admin user."

    def add_arguments(self, parser: Any) -> None:
        parser.add_argument(
            "--email",
            required=True,
            help="Admin user email.",
        )

        parser.add_argument(
            "--password",
            required=True,
            help="Admin user password.",
        )

    def handle(self, *args: Any, **options: Any) -> None:
        UserModel = get_user_model()

        email = options["email"]
        password = options["password"]

        if not email:
            raise CommandError("Email is required.")

        if not password:
            raise CommandError("Password is required.")

        user, created = UserModel.objects.get_or_create(
            email=email,
            defaults={
                "username": email,
            },
        )

        user.username = email
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        if created:
            self.stdout.write(
                self.style.SUCCESS("Admin user created successfully.")
            )
        else:
            self.stdout.write(
                self.style.SUCCESS("Admin user updated successfully.")
            )