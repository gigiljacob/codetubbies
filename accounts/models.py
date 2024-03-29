import os

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from core.settings import BASE_DIR
from utils.sent_email_template import send_email


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email))

        user.is_active = False
        user.set_password(password)
        user.save(using=self._db)

        subject = "Welcome to TechGig.com! Please verify your email ID"
        template = os.path.join(BASE_DIR, 'email_templates')
        send_email(subject, email, template)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    profession_choice = (("P", "Professional"), ("S", "Student"))
    gender_choices = (("M", "Male"), ("F", "Female"), ("O", "Other"))

    i_am = models.CharField(verbose_name="I am a", max_length=10, choices=profession_choice)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    gender = models.CharField(max_length=5, choices=gender_choices)
    company = models.CharField(max_length=255)
    skills = models.CharField(verbose_name="skills I know", max_length=255)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    # REQUIRED_FIELDS = ["i_am", "name", "gender", "company", "skills"]
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
