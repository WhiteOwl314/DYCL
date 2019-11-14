from django.urls import path
from . import views

app_name = "gallerys"

urlpatterns = [
    path('', views.index, name="index"),
]
