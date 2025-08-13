from django.shortcuts import render ,redirect
from django.urls import reverse_lazy 
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")

        # Validatsiya sectioni

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Bu username allaqachon mavjud.")
            return render(request, "registration/signup.html")

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Bu email allaqachon ro'yxatdan o'tgan.")
            return render(request, "registration/signup.html")

        if len(password) < 6:
            messages.error(request, "Parol kamida 6 ta belgidan iborat bo‘lishi kerak.")
            return render(request, "registration/signup.html")

        if "@" not in email or "." not in email:
            messages.error(request, "Email manzili noto‘g‘ri formatda.")
            return render(request, "registration/signup.html")
        
        user = CustomUser(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
            )
        user.set_password(password)
        user.save()

        return redirect("login")  # success_url kabi ishlaydi
    return render(request, "registration/signup.html")

def logout_view(request):
    logout(request)
    return redirect("home")