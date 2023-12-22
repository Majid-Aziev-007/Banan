from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Админ Панель
    path("admin/", admin.site.urls),
    
    # Основное приложение
    path('', include('finance.urls', namespace='finance')),

    # Авторизация пользователей
    path('auth/', include('users.urls')),
]
