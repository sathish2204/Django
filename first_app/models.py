from django.db import models



class students(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    salary=models.IntegerField()
    city=models.CharField(max_length=50)