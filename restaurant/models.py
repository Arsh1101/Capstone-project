from django.db import models


# Create your models here.
class Menu(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests =  models.IntegerField()
    BookingDate = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.Name

class Booking(models.Model):
    Title = models.CharField(max_length=255)
    Price =  models.DecimalField(decimal_places=2,max_digits=10)
    Inventory = models.IntegerField()

    def __str__(self) -> str:
        return self.Title