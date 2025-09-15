\# Retrieve and display attributes of a Book instance

from bookshelf.models import Book

book = Book.objects.get(title="1984")

book.id, book.title, book.author, book.publication\_year



\# Expected Output 

(2, '1984', 'George Orwell', '1949')

