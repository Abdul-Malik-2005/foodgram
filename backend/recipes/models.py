import string
import random

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint

from users.models import User
from recipes.constants import (INGR_NAME_LENGTH, INGR_UN_LENGTH, MAX, MIN,
                               RECIPE_NAME_LENGTH, TAG_LENGTH,
                               MAX_SHORT_LINK_CODE)


class Tag(models.Model):
    name = models.CharField('Название', max_length=TAG_LENGTH, unique=True)
    slug = models.SlugField(
        'Уникальный слаг', max_length=TAG_LENGTH, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField('Название', max_length=INGR_NAME_LENGTH)
    measurement_unit = models.CharField(
        'Единица измерения', max_length=INGR_UN_LENGTH)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        constraints = [
            UniqueConstraint(
                fields=['name', 'measurement_unit'],
                name='unique_name_measurement')
        ]

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        'Recipe',
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
    )
    amount = models.PositiveSmallIntegerField(
        'Количество в рецепте',
        validators=[
            MinValueValidator(MIN),
            MaxValueValidator(MAX)
        ]
    )

    class Meta:
        verbose_name = 'Рецепт-ингредиент'
        verbose_name_plural = 'Рецепты-ингредиенты'


class Recipe(models.Model):
    name = models.CharField('Название', max_length=RECIPE_NAME_LENGTH)
    image = models.ImageField(
        'Изображениe',
        upload_to='recipes/images/',
        null=True,
        default=None
    )
    text = models.TextField('Описание')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='recipes',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through=RecipeIngredient,
        blank=False,
        verbose_name='Список ингридиентов',
        related_name='recipes',
    )
    tags = models.ManyToManyField(
        Tag,
        blank=False,
        verbose_name='Список тэгов',
        related_name='recipes',
    )
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления',
        validators=[
            MinValueValidator(MIN),
            MaxValueValidator(MAX)
        ]
    )
    short_link = models.URLField(unique=True, blank=True, null=True)
    full_link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-id',)

    def __str__(self):
        return self.name


class Favourite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favorites',
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='favorites',
    )

    class Meta:

        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        constraints = [
            UniqueConstraint(fields=['user', 'recipe'],
                             name='unique_fav_user_recipe')
        ]


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='shopping_carts',
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='shopping_carts',
    )

    class Meta:
        verbose_name = 'Корзина покупок'
        verbose_name_plural = 'Корзина покупок'
        constraints = [
            UniqueConstraint(fields=['user', 'recipe'],
                             name='unique_shop_user_recipe')
        ]


class ShortenedLinks(models.Model):
    """Модель для хранения пар "длинная ссылка-короткий индекс"."""

    original_url = models.URLField()
    short_link_code = models.CharField(
        max_length=MAX_SHORT_LINK_CODE, unique=True
    )

    def save(self, *args, **kwargs):
        """
        Автоматическое добавление короткого кода.
        Если код уже есть в базе, то код не генерируется.
        """
        if not self.short_link_code:
            self.short_link_code = self.generate_short_code()
        super(ShortenedLinks, self).save(*args, **kwargs)

    def generate_short_code(self):
        """Генератор коротких кодов."""
        characters = string.ascii_letters + string.digits
        while True:
            short_link_code = "".join(
                random.choices(characters, k=MAX_SHORT_LINK_CODE)
            )
            if not ShortenedLinks.objects.filter(
                short_link_code=short_link_code
            ).exists():
                return short_link_code

    def __str__(self):
        return self.original_url
