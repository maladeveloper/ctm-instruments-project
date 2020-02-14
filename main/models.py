from django.db import models


class Instrument(models.Model):
    """
    An Instrument to be displayed on the website
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    instrument_image = models.ImageField()
    caption = models.TextField()


    def __str__(self):
        """Return a string representation of the model."""
        return self.name


