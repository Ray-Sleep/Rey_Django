from django.db import models

# Create your models here.
from django.db import models

class UserInfo(models.Model):
    # charField 字符串
    # max_length 最大长度(位数)
    name = models.CharField(max_length=32)
    # intField 整型
    number = models.IntegerField()
    password = models.CharField(max_length=64)



