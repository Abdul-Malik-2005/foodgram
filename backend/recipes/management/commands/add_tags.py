from django.core.management.base import BaseCommand
from recipes.models import Tag


class Command(BaseCommand):
    help = "Добавляет теги в базу данных"

    def handle(self, *args, **kwargs):
        tags = [
            {"name": "Завтрак", "slug": "breakfast"},
            {"name": "Обед", "slug": "lunch"},
            {"name": "Ужин", "slug": "dinner"},
        ]

        for tag_data in tags:
            tag, created = Tag.objects.get_or_create(
                slug=tag_data["slug"],
                defaults={"name": tag_data["name"]},
            )
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f'Добавлен тег: {tag.name}')
                )
            else:
                self.stdout.write(f'Тег {tag.name} уже существует')
