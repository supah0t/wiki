from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length = 40)
    textBody = models.TextField(blank=False, null=False)