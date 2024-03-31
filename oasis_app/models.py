from django.db import models

# Create your models here.

class Prompt(models.Model):
    prompt1 = models.CharField(max_length=200, default = '', null=False)
    feeling = models.CharField(max_length = 200, default = '', null=False)
    stress_level = models.CharField(max_length = 200, default = '', null=False)

    def __str__(self):
        return self.feeling
