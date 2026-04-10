from django.urls import path
from . import views

app_name = "onboarding"

urlpatterns = [
    path('', views.onboarding_start, name='start'),
    path('stage/', views.onboarding_stage, name='stage'),
]