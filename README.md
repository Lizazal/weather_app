# weather_app
App for checking weather using OpenWeather API

Это Django-приложение для отображения погоды в заданном городе в текущий момент.
Для получения погоды использовалась API https://openweathermap.org/current
Чтобы получить свой ключ, необходимо зарегестрироваться на сайте.

Оно умеет:
- Выводить данные о текущей погоде в городе
- Подсказывать какой город хочет ввести пользователь
- При повторном посещении сайта предлагается посмотреть погоду в городе, к которому пользователь обращался последним
- Отображается сколько раз вводили какой город - читабельная для человека таблица и JSON

Оно ещё не умеет, но учится:
- Сохранять историю поиска для каждого пользователя

Также:
- Написаны тесты
- Всё помещено в Docker контейнер

## Установка и запуск приложения

### Запуск без Docker

Клонировать репозиторий:

```
git clone https://github.com/Lizazal/weather_app.git
```
Открыть папку проекта:
```
cd weather_app
```
Создать свой .env файл по образцу из env.example
```
touch .env
	echo "SECRET_KEY = 'your_secret_key'" >> .env
	echo "OPENWEATHERMAP_API_KEY = 'your_api_key'" >> .env
```
Выполнить запуск проекта с помощью Bash-скрипта:
```
setup.sh
```
Открыть приложение по адресу:
```
http://localhost:8000/
```

### Запуск через Docker:
```
git clone https://github.com/Lizazal/weather_app.git
cd weather_app
docker-compose up --build
```
Открыть приложение по адресу:
```
http://localhost:8000/
```

### Всё вручную
Требуется добавить .env со своими ключами:
```
git clone https://github.com/Lizazal/weather_app.git
cd weather_app
touch .env
echo "SECRET_KEY = 'your_secret_key'" >> .env
echo "OPENWEATHERMAP_API_KEY = 'your_api_key'" >> .env
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```





Для использования приложения устройство должно быть подключено к интернету. Если сервер OpenWeatherMap перегружен или у пользователя медленное соединение, запрос может не успеть завершиться вовремя. Также бесплатные планы OpenWeatherMap имеют ограничения на количество запросов в минуту.

Для поиска причины ошибки необходимо:
- Проверить верен ли API-ключ
- Проверить сетевое соединение
```
ping api.openweathermap.org
```
Если оба пункта выполнены, можно вызвать curl для проверки соединения:
```
curl -I "https://api.openweathermap.org/data/2.5/weather?q=London"

```
С использованием API-ключа:
```
curl "http://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY"
```
Оптимальный вариант для проверки с использованием API-ключа и выводом полной информации:
```
curl -v "http://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY"
```
Если соединение сбрасывается, проверьте наличие блокировок или ограничений со стороны провайдера или в локальной сети. Можно попробовать выполнить запрос с другого устройства или в другой сети, чтобы локализовать проблему. Также иногда серверы могут быть недоступны.

При возникновении такой проблемы часто стоит попробовать выполнить запрос ещё раз немного позже.