from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import Book, CustomUser


# Register models.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display Book bibliographic information
    list_display = ("title", "author", "publication_year")

    # Filter search
    list_filter = ("author", "publication_year")

    # Search by title or author
    search_fields = ("title", "author")

# CustomUser
class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["email", "date_of_birth", "profile_photo"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get(password1)
        password2 = self.cleaned_data.get(password2)
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ["email", "password", "date_of_birth", "profie_photo", "is_active", "is_admin"]

class ModelAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    # The fields to be used in displaying the CustomUser model.
    list_display = ["email", "password", "date_of_birth", "profie_photo"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["date_of_birth", "profile_photo"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]

    # Override get_fieldsets with add_fieldsets
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2", "date_of_birth", "profile_photo"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []

# Register the new UserAdmin
admin.site.register(CustomUser, UserAdmin)

# Unregister the Group model from admin
admin.site.unregister(Group)