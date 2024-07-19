from django.db import models

# Создание модели для сохранения истории поиска
# Содержит поля: город, количество просмотров погоды в городе (для всех пользователей)
# Добавлено поле timestamp для возможности сбора статистики по времени просмотра погоды в городах

class SearchHistory(models.Model):
    city = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.city
