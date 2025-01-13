from django.db import models

# Create your models here.


class Services(models.Model):
    title = models.CharField(max_length=100)
    disc = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class SubService(models.Model):
    title = models.CharField(max_length=100)
    ps = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='sub_services')

    def __str__(self):
        return self.title