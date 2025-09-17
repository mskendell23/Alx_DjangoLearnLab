from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet, BookAPIView

router = DefaultRouter()
router.register(r"books_all", BookViewSet, basename="book_all")

urlpatterns = [
    path("", views.api, name="api"),
    path("books/", BookList.as_view(), name="book-list"),
    path("", include("router.urls")),
    path("", BookAPIView.as_view(), name="book_api")
]