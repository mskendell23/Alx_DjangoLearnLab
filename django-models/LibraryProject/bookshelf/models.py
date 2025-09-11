from django.db import models

# Book Model.
class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} published in the year {self.publication_year}"
