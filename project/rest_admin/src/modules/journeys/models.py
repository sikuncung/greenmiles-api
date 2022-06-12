from django.db import models
from rest_admin.src.modules.users.models import Profile

MRT = "MRT"
TRAIN = "Train"
BUS = "Bus"
PRIVATE_CAR = "Car"
GRABBIKE = "GrabBike"
GRABCAR = "GrabCar"

JOURNEY_OPTION = (
    (MRT, MRT),
    (TRAIN, TRAIN),
    (BUS, BUS),
)

TYPE_VEHICLE_OPTION = (
    (MRT, MRT),
    (TRAIN, TRAIN),
    (BUS, BUS),
    (PRIVATE_CAR, PRIVATE_CAR),
    (GRABCAR, GRABCAR),
    (GRABBIKE, GRABBIKE),
)

class Journeys(models.Model):

    title = models.CharField("Title", max_length=150, null=True)
    start_point = models.CharField("Start Point", max_length=150, null=True)
    end_point = models.CharField("End Point", max_length=150, null=True)
    distance = models.DecimalField('Distance', max_digits=15, decimal_places=2, null=True) 
    miles = models.DecimalField('Distance', max_digits=15, decimal_places=2, null=True) 
    date = models.DateField("Date", null=True)
    user_id = models.IntegerField("User",null=True)
    type = models.CharField("Journey Type", max_length=32, choices=JOURNEY_OPTION, blank=True, null=True)
    emission_occured = models.DecimalField('Emission Occured', max_digits=15, decimal_places=2, null=True) 
    emission_actual = models.DecimalField('Emission Actual', max_digits=15, decimal_places=2, null=True) 
    emission_reduced = models.DecimalField('Emission Reduced', max_digits=15, decimal_places=2, null=True) 
    journey_map = models.TextField('Journey Map', null=True)
    lat_start_point = models.DecimalField("Lat start point", max_digits=12, decimal_places=6, null=True)
    long_start_point = models.DecimalField("Long start point", max_digits=12, decimal_places=6, null=True)
    lat_end_point = models.DecimalField("Lat end point", max_digits=12, decimal_places=6, null=True)
    long_end_point = models.DecimalField("Long end point", max_digits=12, decimal_places=6, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.id)

    class Meta(object):
        """ Meta : for Journey metadata."""
        ordering = ['-created_at']
        db_table = "journeys"
        verbose_name = "Journey"
        verbose_name_plural = "Journeys"


class JourneyDetail(models.Model):

    journey = models.ForeignKey(
        Journeys,
        on_delete=models.CASCADE,
        verbose_name="Journey",
        related_name="journey_id",
        null=True,
        blank=True,
    )
    
    start_point = models.CharField("Start Point", max_length=150, null=True)
    end_point = models.CharField("End Point", max_length=150, null=True)
    distance = models.DecimalField('Distance', max_digits=15, decimal_places=2, null=True) 
    emission = models.DecimalField('Emission', max_digits=15, decimal_places=2, null=True) 
    order = models.IntegerField("Order", null=True)
    lat_start_point = models.DecimalField("Lat start point", max_digits=12, decimal_places=6, null=True)
    long_start_point = models.DecimalField("Long start point", max_digits=12, decimal_places=6, null=True)
    lat_end_point = models.DecimalField("Lat end point", max_digits=12, decimal_places=6, null=True)
    long_end_point = models.DecimalField("Long end point", max_digits=12, decimal_places=6, null=True)
    vehicle_type = models.CharField("Vehicle Type", max_length=32, choices=TYPE_VEHICLE_OPTION, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.user.name, self.vehicle_type)

    class Meta(object):
        """ Meta : for Journey Detail metadata."""
        ordering = ['-created_at']
        db_table = "journey_details"
        verbose_name = "Journey Detail"
        verbose_name_plural = "Journey Details"


