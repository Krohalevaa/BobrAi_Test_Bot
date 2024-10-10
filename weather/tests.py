from django.test import TestCase
from .models import RequestLog


class RequestLogTestCase(TestCase):
    def setUp(self):
        RequestLog.objects.create(
            user_id="12345",
            command="/weather Moscow",
            response="Weather data")

    def test_log_creation(self):
        log = RequestLog.objects.get(user_id="12345")
        self.assertEqual(log.command, "/weather Moscow")
