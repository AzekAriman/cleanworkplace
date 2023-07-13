from django.db import models


class Club(models.Model):
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address


class Camera(models.Model):
    ip = models.CharField(max_length=200)
    location = models.CharField(max_length=150, null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)


class Picture(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time = models.DateTimeField(auto_now_add=True)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
