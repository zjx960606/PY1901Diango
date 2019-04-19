from django.db import models

# Create your models here.

class WenTi(models.Model):
    question = models.CharField(max_length=50)

    def __str__(self):
        return self.question

class TouPiao(models.Model):
    cont = models.CharField(max_length=50)
    num = models.IntegerField(default=0)
    twen = models.ForeignKey(WenTi, on_delete=models.CASCADE)

    def __str__(self):
        return self.cont