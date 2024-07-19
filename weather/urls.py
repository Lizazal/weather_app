from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Дополнение названий городов
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    # Страница истории поиска для пользователей
    path('search_history/', views.search_history_view, name='search_history_view'),
    # История поиска в формате JSON
    path('search_history/api/', views.search_history_api, name='search_history_api'),
]