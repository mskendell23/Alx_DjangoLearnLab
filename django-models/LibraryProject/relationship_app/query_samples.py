import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

# Import models
from . models import Author, Book, Library, Librarian

def run_queries():
    # Query all books by a specific author
    author_name = "John Doe"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author.name}:")
        for book in books_by_author:
            print("-", book.title)
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'")
    
    # List all books in a Library
    library_name = "First Library"
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"\nBooks in {library.name}:")
        for book in books_in_library:
            print("-", book.title)
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")
    
    # Retrieve the Librarian for a Library
    librarian_name = "Han Smith"
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian # OnetoOneField related
        print(f"\nThe librarian for {library.name} is {librarian.name}") #OnetoOneField related_name
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")

if __name__ == "__main__":
    run_queries()
    