from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title
    
class Karyawan(models.Model):
    full_name = models.CharField(max_length=40)
    emp_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30,null=True)
    birth_place = models.CharField(max_length=20)
    birth_day = models.DateField(null=True)
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{} - {}".format(self.emp_code, self.full_name)