from django.db import models

class Hours(models.Model):
    DAYS_OF_WEEK = (
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    )
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    opens_at = models.TimeField()
    closes_at = models.TimeField()

class Hotel(models.Model):
    uid = models.UUIDField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    operating_hours = models.ManyToManyField(Hours)

    def __str__(self):
        return self.name


