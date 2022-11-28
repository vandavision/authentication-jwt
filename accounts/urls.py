from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="user_register"),
    path('email-verify/', views.VerifyEmail.as_view(), name="email-verify"),
]
