from django.urls import path
from .views import loginPage, registerPage, logoutPage, docPage

urlpatterns = [
    path('', loginPage, name='login'),
    path('auth/', registerPage, name='auth'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('doc/', docPage, name='docPage')
]