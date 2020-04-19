from django.db import models

class Event(models.Model):
    """Model representing an event."""
    title = models.CharField(
        max_length=200,
        help_text="Enter the title of your event."
    )
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)

    def __str__(self):
        """String representation of the Event."""
        return f"{self.title} - {self.latitude}, {self.longitude}"