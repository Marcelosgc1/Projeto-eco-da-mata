from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    desctiption = models.CharField(max_length=800)
    social_network_link = models.URLField(max_length=200)
    telephone_number = models.CharField(max_length=20) # perhaps we can use 'django-phonenumber-field' extension.
    email = models.EmailField(max_length=254)
    #community_key = models.ForeignKey("app.Model", on_delete=models.CASCADE) # has to be implemented after those models been created
    #event_key = models.ForeignKey("app.Model", on_delete=models.CASCADE) # has to be implemented after those models been created

    def __str__(self):
        return self.name + '\n' + self.desctiption
    
class Management(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    #people = models.ForeignKey("app.Model", on_delete=models.CASCADE) # has to be implemented after those models been created

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
    adress = models.CharField(80, null=False) # Using an Address class with fields like city and neighborhood is also a possibility
    location = models.CharField(100);
    link = models.TextField(null=False); # The approach of an Link class with social media, webpage links and stuff could suit better
    class Format(models.IntegerChoices):
        IN_PERSON = 1, ('IN_PERSON'),
        ONLINE = 2, ('ONLINE'),
        HYBRID = 3, ('HYBRID')
    


class Review(models.Model):
    person_name = models.CharField(80);
    phrase = models.CharField(100);
    class Grade(models.IntegerChoices):
        pass
    