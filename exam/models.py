from django.db import models

# Create your models here.



class phy_easy(models.Model):
    classs = models.IntegerField(default=0)
    category = models.TextField(default='none')
    chapter = models.TextField(default='none')
    option1 = models.TextField(default='none')
    option2 = models.TextField(default='none')
    option3 = models.TextField(default='none')
    option4 = models.TextField(default='none')
    question = models.TextField(default='none')
    question_img = models.TextField(default='none')
    answer = models.TextField(default='none')
    danswer = models.TextField(default='none')
    danswer_img = models.TextField(default='none')
    def __str__(self):
        return self.question