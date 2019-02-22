from django.db import models

# Create your models here.
class Institution(models.Model):
    name = models.CharField(max_length=50,verbose_name='机构名称',blank=True,null=True)