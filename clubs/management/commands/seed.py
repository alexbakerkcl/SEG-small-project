from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from faker.providers import DynamicProvider

class Command(BaseCommand):
    """The database seeder."""
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

        experience_provider = DynamicProvider(
            provider_name="experience",
            elements = ['A','E','I','B','N'],
        )

        self.faker.add_provider(experience_provider)


    def handle(self, *args, **options):
        #print("TODO: The database seeder will be added here...")
        for i in range(100):
            user = User.objects.create_user(
                self.faker.name(),
                experience=faker.experience(),
                statement = self.faker.text(),
                bio = self.faker.text()
            )
