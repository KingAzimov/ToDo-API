from django.db import models
from django.contrib.auth.models import User


class Plan(models.Model):
    sarlavha = models.CharField(max_length=100)
    matn = models.CharField(max_length=100)
    sana = models.DateField()
    holat = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):return self.sarlavha