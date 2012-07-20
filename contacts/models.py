from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
    age = models.CharField(max_length=3)
    email = models.EmailField()

