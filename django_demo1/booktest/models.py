from django.db import models

# Create your models here.
class Tea(models.Model):
    tname = models.CharField(max_length=50)
    tgender = models.BooleanField()
    tage = models.IntegerField(max_length=2)
    def __str__(self):
        return self.tname


class Stu(models.Model):
    sname = models.CharField(max_length=50)
    sgender = models.BooleanField()
    sage = models.IntegerField(max_length=2)
    stea = models.ForeignKey(Tea, on_delete=models.CASCADE)
    def __str__(self):
        return self.sname
