import random

from clubs.models import Club, User
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from faker import Faker


class Command(BaseCommand):
    PASSWORD = "Password123"
    USER_COUNT = 100

    def __init__(self):
        super().__init__()
        self.faker = Faker("en_GB")

    def handle(self, *args, **options):
        user_count = 0
        while user_count < Command.USER_COUNT:
            print(f"Seeding user {user_count}", end="\r")
            try:
                self._create_user()
            except IntegrityError:
                continue
            user_count += 1
        print("User seeding complete")

    @staticmethod
    def _email(first_name, last_name):
        return f"{first_name}.{last_name}@example.org"

    def _create_user(self):
        first_name = self.faker.first_name()
        last_name = self.faker.last_name()
        email = self._email(first_name, last_name)
        username = email
        experience = random.choice("NBIAE")
        statement = self.faker.text(max_nb_chars=520)
        bio = self.faker.text(max_nb_chars=520)
        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            experience=experience,
            statement=statement,
            password=Command.PASSWORD,
            bio=bio,
        )

        User.objects.create(
            username="Jebediah",
            first_name="Jebediah",
            last_name="Kerman",
            email="jeb@example.org",
            password=Command.PASSWORD,
            bio="Hi",
        )

        User.objects.create(
            username="Valentina",
            first_name="Valentina",
            last_name="Kerman",
            email="val@example.org",
            password=Command.PASSWORD,
            bio="Hi",
        )

        User.objects.create(
            username="Billie",
            first_name="Billie",
            last_name="Kerman",
            email="billie@example.org",
            password=Command.PASSWORD,
            bio="Hi",
        )

        # self.club = Club.objects.create(
        #     owner=User.objects.get(username="alex"),
        #     name="Kerbal Chess Club",
        #     location="Qidong",
        #     description="one.",
        # )

        # self.club = Club.objects.create(
        #     owner=User.objects.get(username="alex"),
        #     name="Chess Club first",
        #     location="HuiLong",
        #     description="first.",
        # )

        # self.club = Club.objects.create(
        #     owner=User.objects.get(username="Valentina"),
        #     name="Chess Club secound",
        #     location="LvSi",
        #     description="secound.",
        # )

        # self.club = Club.objects.create(
        #     owner=User.objects.get(username="alex"),
        #     name="Chess Club third",
        #     location="DaXing",
        #     description="third.",
        # )
