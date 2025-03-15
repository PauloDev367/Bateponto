from django.urls import path
from .views import LoginView, RegisterView, CheckImageView

urlpatterns = [
   path('auth/login/', LoginView.as_view(), name='login'),
   path('auth/register/', RegisterView.as_view(), name='register'),
   path('user/check/', CheckImageView.as_view(), name='check.user')
]