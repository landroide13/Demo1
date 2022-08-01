from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import BookViewSet, Index
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    #path('', views.home),
    #path('Index', Index.as_view()),
    path('', include(router.urls)),
]








