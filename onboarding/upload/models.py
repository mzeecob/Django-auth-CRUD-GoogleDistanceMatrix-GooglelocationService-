from django.db import models

# Create your models here.


class Photo(models.Model):
    image_name = models.CharField(max_length=250)
    image_view = models.ImageField(upload_to='Images/')

    def __str__(self):
        return self.image_name
