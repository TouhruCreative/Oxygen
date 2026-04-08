from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            return render(request, "users/login.html", {
                "error": "Неверный email или пароль"
            })

    return render(request, "users/login.html")

def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(email=email).exists():
            return render(request, "users/register.html", {
                "error": "Пользователь уже существует"
            })

        user = User.objects.create_user(
            email=email,
            password=password
        )

        login(request, user)
        return redirect("profile")

    return render(request, "users/register.html")



@login_required
def profile_view(request):
    return render(request, "users/profile.html", {
        "user": request.user
    })

def logout_view(request):
    logout(request)
    return redirect("login")