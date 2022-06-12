from django.db import models

class Profile(models.Model):

    name = models.CharField("Name", max_length=150, null=True)
    level = models.CharField("Level", max_length=150, null=True)
    user_id = models.CharField("User ID", max_length=150, null=True)
    miles = models.DecimalField('Miles', max_digits=15, decimal_places=2, null=True) 
    journeys = models.IntegerField("Quantity", null=True)
    distance = models.DecimalField('Distance', max_digits=15, decimal_places=2, null=True) 
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.level)

    class Meta(object):
        """ Meta : for Profile metadata."""
        ordering = ['-created_at']
        db_table = "profiles"
        verbose_name = "Profiles"
        verbose_name_plural = "Profiles"

