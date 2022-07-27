from django.contrib import admin
from django.urls import path
from . import views
from .views import Index

urlpatterns = [
    path('', views.home),
    path('Index', Index.as_view()),
]








