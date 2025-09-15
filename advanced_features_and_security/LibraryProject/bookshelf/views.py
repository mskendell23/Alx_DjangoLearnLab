from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth import login

# Http Response
def bookshelf(request):
    return HttpResponse("Welcome to this Library.")

# Registering Custom User Model
def register(request):
    if request.method == "POST":
        forms = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("success")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})
