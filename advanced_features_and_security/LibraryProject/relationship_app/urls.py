from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import list_books, LibraryDetails, admin_view, librarian_view, member_view

urlpatterns = [
    # Authentication URLs
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/",auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),

    # Books
    path("", views.relationship_app, name="relationship_app"),
    path("list_books/", views.list_books, name="list_books"),
    path("LibraryDetails/", views.LibraryDetails.as_view, name="LibraryDetails"),
    
    # User Roles with access control
    path("admin-role/", admin_view, name="admin_view"),
    path("librarian-role/", librarian_view, name="librarian_view"),
    path("member-role/", member_view, name="member_view"),

    # CRUD operations
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/", views.edit_book, name="edit_book"),
    path("delete_book/", views.delete_book, name="delete_book"),
]