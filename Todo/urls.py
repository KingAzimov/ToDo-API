from django.contrib import admin
from django.urls import path, include
from asosiy.views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('plans/', PlansAPIView.as_view()),
    path('plan/<int:pk>/', PlanAPIView.as_view()),
    path('get_token/', obtain_auth_token, name='api_token_auth'),
]