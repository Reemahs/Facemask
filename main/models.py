from django.db import models
from django.utils import timezone

# Create your models here.
class Requester(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

class Provider(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

class OrderRequest(models.Model):
    requester = models.ForeignKey(Requester, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True, null=True)
    datePublished = models.DateTimeField('date published')
    complete = models.BooleanField()
    quantity = models.IntegerField(default=1)

    def addProvider(self,provider):
        self.provider = provider

    def changeCompletion(self):
        self.complete = not self.complete

class Item(models.Model): # COMMENT THIS OUT IF IT DOESNT WORK! NOT MIGRATED!
    name = models.CharField(max_length=50)
    quantity = models.IntegerField
    description = models.CharField(max_length=200)
    order = models.ForeignKey(OrderRequest, on_delete=models.CASCADE)
