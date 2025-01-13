from django.urls import path

from api.views import RecipeViewSet

urlpatterns = [
    path('recipes/<int:pk>/', RecipeViewSet.as_view(), name='recipe-detail'),
]
