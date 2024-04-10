from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    

    def __str__(self) -> str:
        return self.name
    