from django.urls import path

from internal_auth import views

app_name = "internal_auth"

urlpatterns = [
    path("login/", views.login_view, name="login"),
]