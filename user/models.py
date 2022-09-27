from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
# User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, nome, password, **other):

        if not email:
            raise ValueError('Usuários devem possuir um endereço de email')

        user = self.model(
            email = self.normalize_email(email),
            nome = nome, **other
        )

        user.set_password(password)

        user.save(using=self._db) #usando banco de dados padrão
        return user

    def create_superuser(self, email, nome, password, **other):
        
        user = self.create_user(
            email,
            password=password,
            nome = nome, 
        )

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

#USER
class User(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=15)
    telefone = models.CharField(max_length=14, unique=True)
    password = models.CharField(max_length=128)
    
    cep = models.CharField(max_length=9)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    last_login = models.DateTimeField(null=True)
    date_joined = models.DateTimeField(default=timezone.now ,null=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.nome