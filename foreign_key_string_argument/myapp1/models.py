from django.db import models


class Tim(models.Model):
    name = models.CharField(max_length=255)
    model = models.ForeignKey('myapp2.Mod')
