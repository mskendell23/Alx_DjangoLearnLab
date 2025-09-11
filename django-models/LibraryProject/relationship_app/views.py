from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import permission_required, user_passes_test, login_required
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from . models import Book
from .models import Library
from . forms import BookForm

# View Request
def relationship_app(request):
    return HttpResponse("Welcome to Relationship App!")

# Function-based View
def list_books(request):
    books = Book.objects.all()
    context = {"list_books": books} 
    return render(request, 'relationship_app/list_books.html', context)

# Class-based View
class LibraryDetails(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = "library"


# Authentication
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user) # login after registration
            return redirect("list_books") # redirect to book list
        else:
            form = UserCreationForm()
        return render(request, "relationship_app/register.html", {"form": form})


# Helper functions for role checks
def is_admin(user):
    return user.is_authenticated and user.profile.role == "Admin"

def is_librarian(user):
    return user.is_authenticated and user.profile.role == "Librarian"

def is_member(user):
    return user.is_authenticated and user.profile.role == "Member"

# User Role with access control
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test
def librarian_view(request):
    return render (request, "relationship_app/librarian_view.html")

@user_passes_test
def member_view(request):
    return render(request, "relationship_app/member_view.html")

 
 # Add Book View
@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})

# Edit Book View
@permission_required("relationship_app.can_change_book", raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm()
    return render(request, "relationship_app/edit_book.html", {"form": form})

# Delete Book View
@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})
