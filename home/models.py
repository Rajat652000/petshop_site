from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    porpose = models.CharField(max_length=122)
    def __str__(self):
        return self.name