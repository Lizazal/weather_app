echo "Создание виртуального окружения"
python -m venv venv
echo "Активация виртуального окружения"
source .\venv\Scripts\activate
echo "Установка зависимостей"
pip install -r requirements.txt
if [ ! -f .env ]; then
    echo ".env не найден. Пожалуйста, создайте файл .env вручную."
    exit 1
fi
echo "Миграции БД"
python manage.py makemigrations
python manage.py migrate
echo "Запуск сервера"
python manage.py runserver
echo "Приложение запущено по адресу http://localhost:8000"
