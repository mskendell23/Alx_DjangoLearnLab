from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .forms import CustomUserCreationForm, ExampleForm
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

# User permissions for book_list
@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request):
    return HttpResponse ("Book edited")

@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    return HttpResponse ("Book created")

@permission_required("bookshelf.can_view", raise_exception=True)
def view_book(request):
    return HttpResponse ("You just Viewed a book")

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request):
    return HttpResponse ("Book deleted")

# Login
def login(request):
    if request.method == "POST":
        forms = ExampleForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("success")