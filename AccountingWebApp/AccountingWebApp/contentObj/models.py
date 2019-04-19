from django.db import models

# Create your models here.
class contentObj(models.Model):
    title = models.TextField()
    description = models.TextField()
    source = models.TextField()