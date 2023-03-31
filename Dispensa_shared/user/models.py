from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    #username = None
    #email = None
    # USERNAME_FIELD = 'id'
    #REQUIRED_FIELDS = ['first_name', 'last_name']

    #company = models.CharField(max_length=30, default="I.p.s")

    # def __str__(self):
    #     return self.first_name + " - " + self.last_name + " - " + self.company
    pass



