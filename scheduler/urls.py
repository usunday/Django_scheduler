from django.urls import path
from scheduler import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('monthlylist/', views.monthlyList, name='monthly'),
    path('schedule/', views.schedule, name='schedule'),
]