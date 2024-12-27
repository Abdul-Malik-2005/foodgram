# recipes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.RecipeListView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('ingredients/', views.IngredientListView.as_view(), name='ingredient-list'),
    path('tags/', views.TagListView.as_view(), name='tag-list'),
]
