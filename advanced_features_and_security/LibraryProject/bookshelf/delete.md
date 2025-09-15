\# Delete Book instance

from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")

book.delete()

(1, {'bookshelf.Book': 1})



\# Confirming deletion

Book.objects.all()

<QuerySet \[<Book: 1984 by George Orwell published in the year 1949>]>

