# В вашем файле user/urls.py
from django.urls import path
from .views import signup_view, login_view, logout_view  # Убедитесь, что вы импортировали представление для регистрации

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),  # Добавьте эту строку
]
