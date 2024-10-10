from django.urls import path
from .views import RequestLogListView, UserRequestLogView

urlpatterns = [
    path('logs/', RequestLogListView.as_view(), name='logs'),
    path('logs/<str:user_id>/', UserRequestLogView.as_view(), name='user_logs'),
]
