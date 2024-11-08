from django.db import models
from django.contrib.auth.models import AbstractUser
from jobxcrm.models import Company



class CustomUser(AbstractUser):
    phone = models.CharField(max_length=13)
    #company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True, blank=True,related_name='users')
    tg_id = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return self.username

