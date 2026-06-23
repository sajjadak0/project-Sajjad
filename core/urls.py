from django.urls import path

from core import views

app_name = "core"
urlpatterns = [
    path("", views.SepehrView, name="sepehr"),
    path("reset-password/", views.ResetPasswordView.as_view(), name="reset-password"),
]
