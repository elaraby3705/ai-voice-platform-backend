from django.urls import path
from .views import RegisterView

urlpatterns = [
    # path('login/', views.LoginView.as_view(), name='auth-login'),
    # path('logout/', views.LogoutView.as_view(), name='auth-logout'),
    # path('me/', views.MeView.as_view(), name='auth-me'),
    path("register/", RegisterView.as_view(), name="auth-register"),
]
