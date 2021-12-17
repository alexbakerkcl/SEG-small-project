import random

from clubs.models import Club, User
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from faker import Faker


class Command(BaseCommand):
    PASSWORD = "Password123"
    USER_COUNT = 20

    def __init__(self):
        super().__init__()
        self.faker = Faker("en_GB")

    def handle(self, *args, **options):
        self._create_bespoke_users()
        user_count = 3
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
        experience = random.choice("NBIAE")
        statement = self.faker.text(max_nb_chars=520)
        bio = self.faker.text(max_nb_chars=520)
        User.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
            experience=experience,
            statement=statement,
            password=Command.PASSWORD,
            bio=bio,
        )
    def _create_bespoke_users(self):
        User.objects.create(
            username="jeb@example.org",
            first_name="Jebediah",
            last_name="Kerman",
            email="jeb@example.org",
            password=Command.PASSWORD,
            experience=random.choice("NBIAE"),
            bio=self.faker.text(max_nb_chars=520),
            statement=self.faker.text(max_nb_chars=520),
        )

        User.objects.create(
            username="val@example.org",
            first_name="Valentina",
            last_name="Kerman",
            email="val@example.org",
            password=Command.PASSWORD,
            experience=random.choice("NBIAE"),
            bio=self.faker.text(max_nb_chars=520),
            statement=self.faker.text(max_nb_chars=520),
        )

        User.objects.create(
            username="billie@example.org",
            first_name="Billie",
            last_name="Kerman",
            email="billie@example.org",
            password=Command.PASSWORD,
            experience=random.choice("NBIAE"),
            bio=self.faker.text(max_nb_chars=520),
            statement=self.faker.text(max_nb_chars=520),
        )

    # def _create_bespoke_user(self):
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
