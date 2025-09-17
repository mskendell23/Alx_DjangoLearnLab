from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields 

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]
