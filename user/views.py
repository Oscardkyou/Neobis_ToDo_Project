from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправление на главную страницу после успешного входа
            else:
                form.add_error(None, 'Неверное имя пользователя или пароль')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Перенаправление на страницу входа после выхода


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохранение нового пользователя
            login(request, user)  # Автоматический вход пользователя после регистрации
            return redirect('home')  # Перенаправление на главную страницу после регистрации
    else:
        form = UserCreationForm()  # Пустая форма для нового пользователя
    return render(request, 'signup_view.html', {'form': form})