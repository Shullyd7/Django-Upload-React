from django.db import models

# Create your models here.

class File(models.Model):
    date_time = models.CharField(max_length=120)
    close = models.IntegerField()
    high = models.IntegerField()
    low = models.IntegerField()
    open = models.IntegerField()
    volume = models.IntegerField()
    instrument = models.CharField(max_length=10)


    def __str__(self):
        return self.date_time
