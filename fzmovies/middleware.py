from django.http import HttpResponseRedirect
from django.urls import reverse

class Handle404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 404:
            return HttpResponseRedirect(reverse('home'))

        return response

# myproject/middleware.py
from django.http import HttpResponseForbidden

class AdminIPRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Restrict admin URL access
        if request.path.startswith('/secret/') and request.META.get('REMOTE_ADDR') != '127.0.0.1':
            # Redirect to home page
            return HttpResponseRedirect(reverse('home'))
        return self.get_response(request)