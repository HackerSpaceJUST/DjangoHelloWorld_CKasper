from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=4000)
    applicands = models.ManyToManyField(User, blank=True, related_name='applicands')

    def __str__(self):
        return self.title
