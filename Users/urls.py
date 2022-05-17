from django.urls import path
from .views import dashboard, loginView, activate, signup



urlpatterns = [
    path('', loginView, name='login'),
    path('user/dashboard', dashboard, name="home"),
    path('register/', signup, name = 'register'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate, name='activate'), 
]