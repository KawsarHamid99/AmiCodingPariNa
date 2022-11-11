from django.db import models
# Create your models here.
from django.contrib.auth.models import User,AbstractUser



class Payload(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    input_value=models.CharField(max_length=100)
    timestamp=models.DateTimeField()