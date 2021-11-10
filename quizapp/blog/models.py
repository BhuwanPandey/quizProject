from django.db import models
from django.core.exceptions import ValidationError



class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    detail=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def clean(self):
        getdata=Category.objects.filter(name__contains=self.name)
        if getdata:
            raise ValidationError(f"{self.name} is already exist")

    def __str__(self):
        return self.name


class Quiz(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory=models.CharField(max_length=200)
    totalmarks=models.CharField(max_length=100)
    numberofquestion=models.CharField(max_length=100)
    activestatus=models.BooleanField()

    class Meta:
        unique_together=('category','subcategory',)

    def clean(self):
        getdata=Quiz.objects.filter(subcategory__contains=self.subcategory)
        if getdata:
            raise ValidationError(f"{self.subcategory} is already exist")

    def __str__(self):
        return f'{self.category}-{self.subcategory}'


class Question(models.Model):
    mode=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    mark=models.CharField(max_length=200)
    level=models.CharField(max_length=200)
    date_post=models.DateField(null=True,blank=True)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)

    class Meta:
        unique_together=('mode','name',)

