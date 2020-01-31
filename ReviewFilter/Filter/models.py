from django.db import models

# Create your models here.

class Review(models.Model):
    decision = models.CharField(max_length=100, blank=False)
    hotel    = models.CharField(max_length=100)
    polarity = models.CharField(max_length=100)
    source   = models.CharField(max_length=100)
    text     = models.CharField(max_length=10000)


    def __str__(self):
        return 'decision : {0} hotel : {1} polarity : {2} source : {3} text : {4}'.format(str(self.decision),str(self.hotel),str(self.polarity),str(self.source),str(self.text))