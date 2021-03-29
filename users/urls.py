from django.urls import path
from . import views
from .views import SignUpView

app_name = "users"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", SignUpView.as_view(), name="signup"),
    path("register", views.register_view, name="register"),
]
