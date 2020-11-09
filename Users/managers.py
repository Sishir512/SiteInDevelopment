
# For information check  https://testdriven.io/blog/django-custom-user-model/ && last section of https://docs.djangoproject.com/en/3.1/topics/auth/customizing/


'''
A Manager is the interface through which database query operations are provided to Django models .
So we need to add a custom Manager, by subclassing BaseUserManager, that uses an email as the unique identifier instead of a username.
'''



from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class FocusUsUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, username, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username , password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError(_('Superuser must have is_admin=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, username, password, **extra_fields)


