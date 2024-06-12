from django.db import models

class list(models.Model):
    pass
# Create your models here.
class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(list, on_delete=models.CASCADE, default = None)
    pass
