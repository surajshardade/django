from django.db import models
from datetime import datetime
# Create your models here.
class Category(models.Model):
  ids=models.AutoField(primary_key=True)
  name=models.CharField(max_length=50)
  desc=models.TextField()

  def __str__(self):
    return self.name

class Location(models.Model):
  ids=models.AutoField(primary_key=True)
  name=models.CharField(max_length=50)
  desc=models.TextField()

  def __str__(self):
    return self.name


class Asset(models.Model):

  ID=models.AutoField("Asset ",primary_key=True)
  Label = models.CharField(max_length=100, blank=True, default='')
  Description = models.TextField()
 
  Assignee=models.CharField(max_length=50)
  
  SerialNo=models.CharField(max_length=100,default='123456')
  model=models.CharField(max_length=50)
  warranty=models.CharField(max_length=50)
  #ctime=models.DateTimeField(auto_now_add=True,default=datetime.now().strftime("%c"),editable=False)
  #mtime = models.DateTimeField(auto_now=True,default=datetime.now().strftime("%c"))
  ctime=models.DateTimeField(auto_now_add=True,editable=False)
  mtime = models.DateTimeField(auto_now=True)
  image=models.URLField(blank=True)
  Category=models.ForeignKey('Category',on_delete=models.CASCADE)
  Location=models.ForeignKey('Location',on_delete=models.CASCADE)
