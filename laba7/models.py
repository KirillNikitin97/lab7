from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    class Meta:
        db_table = "Customer"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1)
    password = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30, default='1234')
    email = models.EmailField(max_length=45, default="home@mail.ru")
    photo = models.FileField(upload_to='photo/', blank=True, default='photo/default.png')