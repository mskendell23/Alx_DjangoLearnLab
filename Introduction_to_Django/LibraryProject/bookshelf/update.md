\# Update Book instance

from bookshelf.models import Book

book = Book.objects.get(title="1984")

book.title = "Nineteen Eighty-Four"

book.save()

book



\# Expected Output

<Book: Nineteen Eighty-Four by George Orwell published in the year 1949>

