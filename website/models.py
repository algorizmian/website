from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name