from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=255,verbose_name="Имя автора")
    phone = models.CharField(max_length=255)
    emails = models.EmailField()
    mssg = models.TextField()
    dates = models.DateField()

    def __str__(self):
        return self.name