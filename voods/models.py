from django.db import models

class Vood(models.Model):
    name= models.CharField(max_length=40)
    description= models.CharField(max_length=500)

    def __str__(self):
        return self.name