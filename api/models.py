from django.db import models
from django.conf import settings
from django.db.models.base import Model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserManager(BaseUserManager):
    def create_user(self, email, username, password, teams, groups):
        if not email:
            raise ValueError("Users must have email")
        if not username:
            raise ValueError("Users must have Username")
        if not password:
            raise ValueError("Users must set Password")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password,
            teams=teams,
            groups=groups
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        if not email:
            raise ValueError("Users must have email")
        if not username:
            raise ValueError("Users must have Username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=55, unique=True)
    username = models.CharField(verbose_name='username', max_length=50, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    # field to login a user
    USERNAME_FIELD = 'email'

    # Required Field to create users
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return f'{self.username} {self.email}'
    #
    # def has_perm(self, perm, obj=None):
    #     return self.has_perm(perm)
    #
    # def has_module_perms(self, app_label):
    #     return self.has

class FireAndIce(models.Model):
    emoji = models.CharField(max_length=55)
    date = models.DateTimeField()

    def __str__(self):
            return f'{self.emoji}'

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=55)
    date = models.DateField()

    def __str__(self):
        return f'{self.title}'

    # class Meta:
    #     permissions = (("view_event", "can view all events"), ("add_event", "can add event"))
