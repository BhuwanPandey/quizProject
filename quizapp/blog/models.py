from django.db import models

# Create your models here.

class Quiz(models.Model):
    category=models.CharField(max_length=200)
    subcategory=models.CharField(max_length=200)
    question=models.CharField(max_length=200)
    op1=models.CharField(max_length=200)
    op2=models.CharField(max_length=200)
    op3=models.CharField(max_length=200)
    op4=models.CharField(max_length=200)
    ans=models.CharField(max_length=200)