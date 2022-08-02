from django.db import models


class UserDetail(models.Model):
    name = models.CharField(max_length=264)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()

    def __str__(self):
        return self.name
