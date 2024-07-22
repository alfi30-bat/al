from django.db import models

# Create your models here.

class use_info(models.Model):
    username = models.TextField(default='none')
    email = models.TextField(default='none')
    classs = models.TextField(default='none')
    category = models.TextField(default='none')
    score =models.IntegerField(default=0)
    def __str__(self):
        return self.question