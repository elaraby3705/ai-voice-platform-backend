# accounts/views.py
from django.views import View
from django.http import JsonResponse

class LogoutView(View):
    def post(self, request):
        return JsonResponse({'message': 'Logged out successfully'})
