from django.db import models


class Movies(models.Model):
    pic = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255)
    whatched = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
