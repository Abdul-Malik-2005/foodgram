import os
import django
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from recipes.models import Recipe, Ingredient, Tag, User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodgram.settings')
django.setup()


class Command(BaseCommand):
    help = 'Добавляет рецепты в базу данных'

    def handle(self, *args, **kwargs):
        user = User.objects.create(username='testuser', password='password')

        tags_data = [
            {'name': 'Закуска'},
            {'name': 'Летнее'},
            {'name': 'Основное'},
            {'name': 'Десерт'}
        ]

        for tag_data in tags_data:
            slug = slugify(tag_data['name'])
            # Если slug уже существует, добавляем суффикс
            counter = 1
            original_slug = slug
            while Tag.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            
            tag = Tag.objects.create(name=tag_data['name'], slug=slug)
            self.stdout.write(self.style.SUCCESS(f"Тег '{tag.name}' с slug '{tag.slug}' добавлен"))

        ingredient1 = Ingredient.objects.create(name='Томаты')
        ingredient2 = Ingredient.objects.create(name='Масло оливковое')
        ingredient3 = Ingredient.objects.create(name='Картофель')
        ingredient4 = Ingredient.objects.create(name='Морковь')
        ingredient5 = Ingredient.objects.create(name='Курица')
        ingredient6 = Ingredient.objects.create(name='Мед')
        ingredient7 = Ingredient.objects.create(name='Шоколад')

        recipes_data = [
            {'name': 'Летний салат', 'tags': [tag1, tag2], 'ingredients': [ingredient1, ingredient2], 'text': 'Это летний салат', 'cooking_time': 15},
            {'name': 'Картофельное пюре', 'tags': [tag3], 'ingredients': [ingredient3, ingredient2], 'text': 'Классическое картофельное пюре', 'cooking_time': 30},
            {'name': 'Запеченная курица', 'tags': [tag3], 'ingredients': [ingredient5, ingredient2], 'text': 'Запеченная курица с пряностями', 'cooking_time': 60},
            {'name': 'Морковный салат', 'tags': [tag1], 'ingredients': [ingredient4], 'text': 'Салат из тертой моркови', 'cooking_time': 10},
            {'name': 'Медовый десерт', 'tags': [tag4], 'ingredients': [ingredient6], 'text': 'Легкий медовый десерт', 'cooking_time': 20},
            {'name': 'Шоколадный торт', 'tags': [tag4], 'ingredients': [ingredient7], 'text': 'Шоколадный торт с кремом', 'cooking_time': 90},
            {'name': 'Салат с курицей', 'tags': [tag1, tag3], 'ingredients': [ingredient1, ingredient2, ingredient5], 'text': 'Салат с курицей и овощами', 'cooking_time': 20},
            {'name': 'Картофель фри', 'tags': [tag3], 'ingredients': [ingredient3], 'text': 'Картофель фри с соусом', 'cooking_time': 25},
            {'name': 'Морковный суп', 'tags': [tag3], 'ingredients': [ingredient4], 'text': 'Легкий суп из моркови', 'cooking_time': 40},
            {'name': 'Куриный суп', 'tags': [tag3], 'ingredients': [ingredient5], 'text': 'Сытный куриный суп', 'cooking_time': 45},
            {'name': 'Шоколадный мусс', 'tags': [tag4], 'ingredients': [ingredient7], 'text': 'Шоколадный мусс с кремом', 'cooking_time': 30},
            {'name': 'Салат с картофелем', 'tags': [tag1, tag3], 'ingredients': [ingredient3, ingredient1], 'text': 'Салат с картофелем и овощами', 'cooking_time': 20},
        ]

        for recipe_data in recipes_data:
            recipe = Recipe.objects.create(
                name=recipe_data['name'],
                author=user,
                text=recipe_data['text'],
                cooking_time=recipe_data['cooking_time'],
                image='tomato.jpg'  # Укажите путь к изображению, если оно есть
            )
            
            # Добавляем ингредиенты и теги к рецепту
            recipe.ingredients.add(*recipe_data['ingredients'])
            recipe.tags.add(*recipe_data['tags'])

            self.stdout.write(self.style.SUCCESS(f"Рецепт '{recipe.name}' добавлен успешно!"))
