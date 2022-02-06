from django.db import router
from django.urls import path, include
from API_Side import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()


router.register('store', views.StoreView, basename='store')


urlpatterns = [
    path('store/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace="rest_framework")),
]