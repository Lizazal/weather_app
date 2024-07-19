# weather_app
App for checking weather using OpenWeather API

Это Django-приложение для отображения погоды в заданном городе в текущий момент.
Для получения погоды использовалась API https://openweathermap.org/current

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

Запуск через Docker:
```
git clone https://github.com/Lizazal/weather_app.git
cd weather_app
docker-compose up --build
```
Открыть приложение по адресу:
```
http://localhost:8000/
```

Возможно всё запустить вручную (требует добавления .env с ключами):
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