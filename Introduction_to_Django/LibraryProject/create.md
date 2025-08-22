\# Create a Book instance

from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication\_year="1949")

book



\# Expected Output

<Book: 1984 by George Orwell published in the year 1949>

