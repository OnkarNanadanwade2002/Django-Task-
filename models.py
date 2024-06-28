from django.db import models
from django.contrib.auth.models import User

class Box(models.Model):
    length = models.FloatField()
    breadth = models.FloatField()
    height = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def area(self):
        return self.length * self.breadth

    @property
    def volume(self):
        return self.length * self.breadth * self.height
