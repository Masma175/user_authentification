from django.urls import path
from .views import dashboard, loginView



urlpatterns = [
    path('', loginView, name='login'),
    path('user/dashboard', dashboard, name="dashboard")
]