from django.db import models
from sorl.thumbnail import ImageField
# Create your models here.
class post(models.Model):
    image = ImageField()
    text = models.CharField(max_length=140, blank=False, null=False)
    def __str__(self):
        return self.text

#class PostDetailView(models.Model):
    






