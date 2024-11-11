from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Account(AbstractUser):
    email = models.CharField(unique=True, max_length=100)
    phone_number = models.CharField(max_length=50)
    date_joined_formatted = models.DateTimeField(auto_now_add=True)
    last_login_formatted = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def get_date_joined(self):
        return self.date_joined_formatted.strftime('%B %d %Y')
    
    def get_last_login(self):
        return self.last_login_formatted.strftime('%B %d %Y')

    def __str__(self):
        return self.email
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
