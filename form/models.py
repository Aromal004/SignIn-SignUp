from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None,**extra_fields):
        if not phone:
            raise ValueError('Users must have an phone number')
        
        user=self.model(phone=phone,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    
    def create_superuser(self, phone, password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        return self.create_user(phone,password,**extra_fields)


class CustomUser(AbstractUser):
    username=None
    phone=models.BigIntegerField(unique='True')
    gender=models.CharField(max_length=6)

    USERNAME_FIELD='phone'
    REQUIRED_FIELDS=[]
    objects = CustomUserManager()

    def __str__(self):
        return str(self.phone)