from django.urls import path
from .views import RegisterView, LoginView, AddressListCreateView, SetDefaultAddressView
from django.http import JsonResponse

def auth_root(request):
    return JsonResponse({'message': 'Auth API root. Use /register/ or /login/'})

urlpatterns=[
    path('', auth_root),
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(), name='login'),
    path('addresses/', AddressListCreateView.as_view(), name='address-list-create'),
    path('addresses/<int:pk>/set-default/', SetDefaultAddressView.as_view(), name='set-default-address'),
]