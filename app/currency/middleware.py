from time import time
from currency.models import RequestResponseLog
from django.utils import timezone


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Засекаем время начала обработки запроса
        start_time = timezone.now()

        response = self.get_response(request)

        # Вычисляем время выполнения запроса
        end_time = timezone.now()
        elapsed_time = (end_time - start_time).total_seconds()

        # Создаем объект RequestResponseLog
        log_entry = RequestResponseLog(
            path=request.path,
            request_method=request.method,
            time=int(elapsed_time)
        )
        log_entry.save()

        return response