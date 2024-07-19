from django.test import TestCase
from django.urls import reverse

# Тесты для views
class WeatherViewsTests(TestCase):

    # Отправка GET запроса для проверки успешной работы страниц (возвращают 200)
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
 
    def test_autocomplete(self):
        response = self.client.get(reverse('autocomplete'), {'term': 'Lon'})
        self.assertEqual(response.status_code, 200)

    def test_search_history_view(self):
        response = self.client.get(reverse('search_history_view'))
        self.assertEqual(response.status_code, 200)

    def test_search_history_api(self):
        response = self.client.get(reverse('search_history_api'))
        self.assertEqual(response.status_code, 200)
