from django.urls import path

from . import views

app_name = 'finance'

urlpatterns = [
    # Анализ доходов и расходов
    path('', views.index, name='index'),

    # Создание дохода или расхода
    path('finance/create/', views.operation_create, name='operation_create'),
]
