from django.contrib import admin
from .models import Book

# Register models.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display Book bibliographic information
    list_display = ("title", "author", "publication_year")

    # Filter search
    list_filter = ("author", "publication_year")

    # Search by title or author
    search_fields = ("title", "author")
