from django.db import models

# Create your models here.

class GeeksModels(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title
