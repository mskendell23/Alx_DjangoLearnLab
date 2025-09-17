from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer # type: ignore

# Http Response
def api(request):
    return HttpResponse("Welcome to this API.")

# BookList
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    context_object_name = "book-list"


    def get_queryset(self):
        queryset = self.queryset
        name_filter = self.request.query_params.get("name", None)
        if name_filter is not None:
            queryset = queryset.filter(name__icontains=name_filter)
            return queryset
        
# CRUD Operations using viewset
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    