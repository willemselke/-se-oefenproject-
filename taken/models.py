from django.db import models

class Taak(models.Model):
    titel = models.CharField(max_length=200)
    is_voltooid = models.BooleanField(default=False)
    aangemaakt_op = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titel

# Create your models here.
