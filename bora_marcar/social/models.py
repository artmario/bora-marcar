from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
  id = models.IntegerField()
  nome = models.CharField(max_length=200)
  desc = models.TextField()
  type = models.CharField(max_length=200)
  inicio = models.DateTimeField(blank=True, null=True)
  fim = models.DateTimeField(blank=True, null=True)
  range  = models.CharField(max_length=200)
  created_date = models.DateTimeField(default=timezone.now)
  end_poll = models.DateTimeField(blank=True, null=True)
  status = models.DateTimeField(blank=True, null=True)
  id_admin = models.IntegerField()
