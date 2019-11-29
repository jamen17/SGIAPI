from django.db import models

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    #imagen = models.ImageField(null=True)
    #propietario = models.IntegerField()
    def __str__(self):
        return self.file.name