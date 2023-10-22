from django.db import models

# Create your models here.
class Teacher(models.Model):
    account=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)
    name=models.CharField(max_length=20)

    class Meta:
        db_table="teacher"

class Student(models.Model):
    name=models.CharField(max_length=20,unique=True)
    age=models.IntegerField()
    isbind=models.BooleanField(default=True)
    teacher=models.ForeignKey("Teacher",on_delete=models.CASCADE)

    class Meta:
        db_table="student"
