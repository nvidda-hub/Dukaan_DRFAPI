from django.contrib import admin
from django.db import router
from django.urls import path, include
from API_Side import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()


router.register('students', views.StudentView, basename='student')


urlpatterns = [
    path('students/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace="rest_framework")),
]