from django.db import models


class Reciepe(models.Model):
    reciepe_name=models.CharField(max_length=100)
    ingradiants= models.TextField()
    process = models.TextField()


    def __str__(self):
        return self.reciepe_name
