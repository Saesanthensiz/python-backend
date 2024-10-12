from django.urls import path
from .import views

urlpatterns = [
    path('', views.tasks_list, name='tasks_list'),
    path('work_list/', views.work_list, name='work_list'),
]
