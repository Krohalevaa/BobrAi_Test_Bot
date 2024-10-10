from rest_framework import serializers
from .models import RequestLog


class RequestLogSerializer(serializers.ModelSerializer):
    """Сериализатор для модели RequestLog."""
    class Meta:
        model = RequestLog
        fields = '__all__'
