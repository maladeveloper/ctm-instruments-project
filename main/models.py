from django.db import models


class Instrument(models.Model):
    """
    An Instrument to be displayed on the website
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    caption = models.TextField()
    youtube_url = models.CharField(max_length=100, default="https://www.youtube.com/watch?v=7IR7xB3VPPc")
    youtube_code = None
    image_url = models.TextField(default="image.png")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.youtube_code = self.change_url()

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

    def change_url(self):
        old_string = self.youtube_url
        new_string = ""
        i = len(old_string) - 1
        while old_string[i] != "=":
            new_string = new_string + old_string[i]
            i=i-1

        return new_string[::-1]


