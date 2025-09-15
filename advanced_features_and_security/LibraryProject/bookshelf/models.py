from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin

# Book Model.
class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} published in the year {self.publication_year}"

# Custom User Model
class CustomUserManager(UserManager):
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

        return self.create_user(self, email, password, **extra_fields)
    

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length= 100, blank=True)
    last_name = models.CharField(max_length= 100, blank=True)
    email = models.EmailField(unique=True) 
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth"] 

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj = None):
        "Does the user have a specific permission?"
        return True
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the 'app_label'?"
        return True
    
    def is_staff(self):
        "Is user a member of staff?"
        return self.is_admin