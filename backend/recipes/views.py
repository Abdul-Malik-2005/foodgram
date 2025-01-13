from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from recipes.models import Recipe


def redirect_to_full_recipe(request, pk):
    """
    Редиректит пользователя с короткой ссылки на полный URL рецепта.
    """
    recipe = get_object_or_404(Recipe, pk=pk)
    full_url = reverse('recipe-detail', kwargs={'pk': recipe.id})
    return HttpResponseRedirect(full_url)
