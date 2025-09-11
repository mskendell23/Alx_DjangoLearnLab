from django.urls import path
from . import views
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path("", views.relationship_app, name="relationship_app"),
    path("list_books/", views.list_books, name="list_books"),
    path("LibraryDetails/", views.LibraryDetails.as_view, name="LibraryDetails"),
    
    # User Roles with access control
    path("admin-role/", admin_view, name="admin_view"),
    path("librarian-role/", librarian_view, name="librarian_view"),
    path("member-role/", member_view, name="member_view"),

    # CRUD
    path("books/add/", views.add_book, name="add_book"),
    path("books/edit/<int:pk>/", views.edit_book, name="edit_book"),
    path("books/delete/<int:pk>/", views.delete_book, name="delete_book"),
]