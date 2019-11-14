from django.db import models


class Gallery(models.Model):
    name = models.CharField(max_length=100, )
    file = models.ImageField(upload_to="gallery")

    def __str__(self):
        return self.name
