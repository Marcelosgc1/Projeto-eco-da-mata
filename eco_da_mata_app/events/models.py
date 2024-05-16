from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    class Category(models.TextChoices):
        LECTURE = 'LC', ('Lecture'), 
        FAIR = 'FR', ('Fair'), 
        CONFERENCE = 'CF', ('Conference')
        WORKHSOP = 'WK', ('Workshop'), 
        SEMINARY = 'SM', ('Seminary'), 
        ART_EXHIBITION = 'AE', ('Art Exhibition'), 
        FESTIVAL = 'FV', ('Festival'),
        OTHERS = 'OT', ('Others')
    adress = models.CharField(max_length=80, null=False) # Using an Address class with fields like city and neighborhood is also a possibility
    location = models.CharField(max_length=100);
    link = models.TextField(null=False); # The approach of an Link class with social media, webpage links and stuff could suit better
    class Format(models.IntegerChoices):
        IN_PERSON = 1, ('IN_PERSON'),
        ONLINE = 2, ('ONLINE'),
        HYBRID = 3, ('HYBRID')