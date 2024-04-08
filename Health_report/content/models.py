from django.db import models

# Create your models here.

class User(models.Model):
  user_name  = models.CharField(max_length=20)
  gender = models.CharField(max_length=10)
  
class Report(models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
  report_name = models.CharField(max_length=50)
  report_year = models.CharField(max_length=5)
  diastolic_pressure = models.IntegerField()
  systolic_pressure  = models.IntegerField()
  pulse = models.IntegerField()
  glucose_ac = models.IntegerField()
  hba1c = models.FloatField()
  t_cho = models.IntegerField()
  tg = models.IntegerField()
  hdl_c = models.IntegerField()
  ldl_c = models.IntegerField()
  problems = models.TextField(max_length=200)
  abstract = models.TextField(max_length=1000)
  created_at = models.DateTimeField(auto_now_add=True)


class Arg(models.Model):
  name = models.CharField(max_length=20)
  e_name = models.CharField(max_length=20)
  c_name = models.CharField(max_length=20)
  max = models.IntegerField(blank=True, null=True)
  min = models.IntegerField(blank=True, null=True)
  m_min = models.IntegerField(blank=True, null=True)
  f_min = models.IntegerField(blank=True, null=True)
  unit = models.CharField(max_length=10)
  
