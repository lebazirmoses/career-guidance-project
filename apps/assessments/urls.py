from django.urls import path
from . import views

app_name = 'assessments'

urlpatterns = [
    path('', views.test_list, name='test_list'),
    path('start/', views.start_next_test, name='start_next_test'),  # 🔥 NEW
    
    path('take/<slug:slug>/', views.take_test, name='take_test'),
    path('results/<slug:slug>/', views.test_results, name='test_results'),
]