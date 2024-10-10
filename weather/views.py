from rest_framework import generics
from .models import RequestLog
from .serializers import RequestLogSerializer


class RequestLogListView(generics.ListAPIView):
    """Представление для получения списка всех запросов."""
    queryset = RequestLog.objects.all()
    serializer_class = RequestLogSerializer


class UserRequestLogView(generics.ListAPIView):
    """Представление для получения запросов конкретного пользователя."""
    serializer_class = RequestLogSerializer

    def get_queryset(self):
        """
        Возвращает набор данных, отфильтрованный по `user_id`,
        переданному в параметре URL.
        """
        user_id = self.kwargs['user_id']
        return RequestLog.objects.filter(user_id=user_id)
