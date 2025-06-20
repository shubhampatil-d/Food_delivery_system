from django.urls import path
from .views import RegisterView, LoginView
from django.http import JsonResponse

def auth_root(request):
    return JsonResponse({'message': 'Auth API root. Use /register/ or /login/'})

urlpatterns=[
    path('', auth_root),
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(), name='login'),
]