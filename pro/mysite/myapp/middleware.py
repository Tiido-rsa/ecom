import time
from django.http import HttpResponseForbidden

class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # BEFORE THE VIEW IS CALLED
        print(f'[Middleware] Request Path: {request.path}')
        response = self.get_response(request)
        # AFTER THE VIEW IS CALLED
        print(f'[Middleware] Response Status Code: {response.status_code}')
        return response

class TimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        print(f'[Middleware] Request Duration: {duration:.2f} seconds')
        return response

class BlockIPMiddleware:

    blocked_ips = []

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        ip = request.META.get('REMOTE_ADDR')
        if ip in self.blocked_ips:
            return HttpResponseForbidden('Access Denied')
        return self.get_response(request)        