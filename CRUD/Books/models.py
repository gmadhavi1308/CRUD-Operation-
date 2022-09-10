from django.db import models

# Create your models here.
class Books(models.Model):
    Title = models.CharField(max_length = 100)
    Author = models.CharField(max_length = 100)
    Edition = models.CharField(max_length = 20)
    Price = models.FloatField()

    class Meta:
        db_table='books'
