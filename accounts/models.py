import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


# def generate_unique_id():
#     """
#     Generates a short, human-friendly, guaranteed-unique public ID
#     for a user, e.g. USR-7F3A9C2D
#     """
#     while True:
#         candidate = 'USR-' + uuid.uuid4().hex[:8].upper()
#         if not User.objects.filter(unique_id=candidate).exists():
#             return candidate


# class User(AbstractBaseUser, PermissionsMixin):
#     # Public, unique, non-guessable identifier shown to the user / used in APIs
#     unique_id = models.CharField(
#         max_length=20, unique=True, editable=False, db_index=True
#     )

#     username = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(unique=True)
#     full_name = models.CharField(max_length=150, blank=True)

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def save(self, *args, **kwargs):
#         if not self.unique_id:
#             self.unique_id = generate_unique_id()
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f'{self.username} ({self.unique_id})'

class User(AbstractBaseUser, PermissionsMixin):

    unique_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        db_index=True
    )

    username = models.CharField(
        max_length=50,
        unique=True
    )

    email = models.EmailField(
        unique=True
    )

    full_name = models.CharField(
        max_length=150,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    profile_pic = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    nid_image = models.ImageField(
        upload_to="nid/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = generate_unique_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.unique_id})"