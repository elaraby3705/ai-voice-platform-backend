from django.urls import path
from .views import RegisterView, LoginView, MeView

urlpatterns = [
    # path('logout/', views.LogoutView.as_view(), name='auth-logout'),
    # path('me/', views.MeView.as_view(), name='auth-me'),
    path("register/", RegisterView.as_view(), name="auth-register"),
    path("login/", LoginView.as_view(), name="auth-login"),
    path("me/", MeView.as_view(),name="me"),
]
