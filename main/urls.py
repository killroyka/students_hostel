from django.contrib import admin
from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('mainpage/', HomePageView.as_view()),
]
