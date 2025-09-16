from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Book Model.
class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} published in the year {self.publication_year}"
    
    class Meta:
        permissions = [
            ("can_view", "Can view a book"),
            ("can_create", "Can create a new book"),
            ("can_edit", "Can edit a book"),
            ("can_delete", "Can delete a book"),
        ]

# Custom User Model
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("No valid email address was entered.")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)
    

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length= 100, blank=True)
    last_name = models.CharField(max_length= 100, blank=True)
    email = models.EmailField(unique=True) 
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to="profiles/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth"] 

    def __str__(self):
        return self.email
    
    
    @property
    def is_staff(self):
        "Is user a member of staff?"
        return self.is_admin