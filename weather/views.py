import requests
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .models import SearchHistory
from .forms import CityForm
from django.db.models import F

def get_weather_data(city):
    # Функция отвечает за получение данных о погоде в заданном городе city
    api_key = settings.OPENWEATHERMAP_API_KEY
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    try:
        # Установка таймаута в 10 секунд, чтобы пользователю не приходилось долго ждать, но у сервера было время ответить
        response = requests.get(url, timeout=10)  
        # Проверяем, что запрос прошел успешно
        response.raise_for_status()  
        return response.json()
    # Возврат информации о возникшей ошибке
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    # Возврат None в случае ошибки
    return None  

def index(request):
    # Проверка для метода POST
    if request.method == 'POST':
        # Создаётся экземпляр формы с данными, переданными POST
        form = CityForm(request.POST)
        # Проверка валидности
        if form.is_valid():
            # Получение названия города из формы
            city = form.cleaned_data['city']
            # Вызов метода для получения погоды
            weather_data = get_weather_data(city)
            # Проверка успешности запроса - данные вернулись и получен код 200 (то есть запрос успешен)
            if weather_data and weather_data.get('cod') == 200:
                # Обновление истории поиска - добавление записи или увеличение счётчика просмотров на 1
                search_history, created = SearchHistory.objects.get_or_create(city=city)
                if created:
                    search_history.count = 1
                else:
                    search_history.count += 1
                search_history.save()
                # Формирование контекста
                context = {'weather_data': weather_data, 'form': form}
                # Передача контекста в шаблон
                response = render(request, 'weather/index.html', context)
                # Записываем имя последнего введённого города в куки
                response.set_cookie('last_city', city)
                return response
            else:
                # Обработка ошибок
                context = {'error': 'City not found or error occurred!', 'form': form}
                return render(request, 'weather/index.html', context)
    # Обработка всех не POST запросов (первое посещение/перезагрузка страницы)
    else:
        # Извлечение последнего введённого города из куки, если он есть
        last_city = request.COOKIES.get('last_city')
        # Создание формы с заполненным городом
        form = CityForm(initial={'city': last_city} if last_city else None)
        # Создание и передача контекста с городом
        context = {'form': form}
        return render(request, 'weather/index.html', context)


def autocomplete(request):
    # Проверяется приходит ли информация о вводе пользователем города
    if 'term' in request.GET:
        # Создаётся сет городов из модели, начинающихся с тех же символов, что и ввод пользователя
        qs = SearchHistory.objects.filter(city__istartswith=request.GET.get('term'))
        cities = list()
        # Название города добавляется в список
        for city in qs:
            cities.append(city.city)
        # Возврат списка подходящих городов
        return JsonResponse(cities, safe=False)
    return JsonResponse([], safe=False)

def search_history_api(request):
    # Достаются записи из таблицы
    search_history = SearchHistory.objects.all().values('city', 'count')
    # Преобразуются в список
    data = list(search_history)
    # Передаются в JSON формате как объекты
    return JsonResponse(data, safe=False)

def search_history_view(request):
    # Достаются записи из таблицы. Для удобного просмотра они сортируются в порядке убывания количества просмотров города
    search_history = SearchHistory.objects.all().order_by('-count')
    # Рендерится страничка для просмотра
    return render(request, 'weather/search_history.html', {'search_history': search_history})
