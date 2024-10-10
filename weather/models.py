from django.db import models


class RequestLog(models.Model):
    """Модель для логирования запросов пользователей бота."""
    user_id = models.CharField(max_length=100)
    command = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    response = models.TextField()

    def __str__(self):
        return f"Request from {self.user_id} at {self.timestamp}"
