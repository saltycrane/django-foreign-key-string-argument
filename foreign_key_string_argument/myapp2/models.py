from django.db import models


class Mod(models.Model):
    name = models.CharField(max_length=100)
