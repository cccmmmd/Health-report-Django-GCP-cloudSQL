from django.db import models

# Create your models here.

class User(models.Model):
  user_name  = models.CharField(max_length=30)
  gender = models.CharField(max_length=30)
  
class Report(models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
  report_name = models.CharField(max_length=50)
  report_year = models.IntegerField()
  diastolic_pressure = models.IntegerField()
  systolic_pressure  = models.IntegerField()
  pulse = models.IntegerField()
  glucose_ac = models.IntegerField()
  hba1c = models.FloatField()
  t_cho = models.IntegerField()
  tg = models.IntegerField()
  hdl_c = models.IntegerField()
  ldl_c = models.IntegerField()
  abstract = models.TextField(max_length=200)
  
