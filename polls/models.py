from django.db import models


class Rebus(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to="static/rebuses")

