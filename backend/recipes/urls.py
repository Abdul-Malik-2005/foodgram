from django.urls import path

from recipes.views import redirect_to_full_recipe

urlpatterns = [
    path('int:pk>', redirect_to_full_recipe),
]
