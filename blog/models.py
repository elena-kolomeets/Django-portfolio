from django.db import models
from datetime import date


class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=date.today)
    text = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
