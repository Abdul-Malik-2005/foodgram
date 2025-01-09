import json

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загружает данные ингредиентов из JSON файла в базу данных'

    def handle(self, *args, **kwargs):
        file_path = './data/ingredients.json'

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                ingredients = json.load(file)

                for ingredient in ingredients:
                    Ingredient.objects.get_or_create(
                        name=ingredient['name'],
                        measurement_unit=ingredient['measurement_unit']
                    )

                self.stdout.write(self.style.SUCCESS('Ингредиенты успешно'
                                                     ' загружены в базу '
                                                     'данных!'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Файл {file_path} не найден"))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR("Ошибка в формате JSON"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ошибка: {e}"))
