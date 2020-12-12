from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)

    unique_id=models.EmailField(max_length=256,default="")
    emid=models.IntegerField()
    joining=models.DateField()
    contact=models.IntegerField()
    designation=models.ForeignKey('Manager.Work',on_delete=models.CASCADE,blank=True,null=True)

    def get_absolute_url(self):
        return reverse("employee_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.user.username

class Work(models.Model):
    jobid=models.IntegerField()
    creation=models.DateField()
    job=models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse("work_list")

    def __str__(self):
        return self.job
