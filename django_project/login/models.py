from django.db import models

# Create your models here.

class BookInfo(models.Model):
    bname = models.CharField(max_length=20)
    btitle = models.CharField(max_length=50)
    pub_data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.bname


class HeroInfo(models.Model):
    hname = models.CharField(max_length=50)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=50)
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.hname

    def skill(self):
        return self.hname
    skill.short_description = '姓名'